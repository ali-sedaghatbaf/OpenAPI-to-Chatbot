from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP, MCPServerStdio
import gradio as gr
import os
from contextlib import AsyncExitStack


class Chatbot:
    async def start(self):
        chat_ui = os.getenv("CHAT_UI")
        if chat_ui == "web":
            await self._start_web()
        elif chat_ui == "cmd":
            await self._start_cmd()
        else:
            raise ValueError("Invalid CHAT_UI value. Use 'web' or 'cmd'.")

    async def _init_agent(self):
        transport = os.getenv("TRANSPORT")
        if transport == "sse":
            host = os.getenv("MCP_HOST")
            port = int(os.getenv("MCP_PORT"))
            mcp_server = MCPServerHTTP(url=f"http://{host}:{port}/sse")
        elif transport == "stdio":
            mcp_server = MCPServerStdio(
                command="uv",
                args=["run", "server_exec.py"],
            )
        else:
            return "Invalid TRANSPORT value. Use 'sse' or 'stdio'."
        self.agent = Agent(
            os.getenv("AI_MODEL"), mcp_servers=[mcp_server], verbose=True
        )
        return "Agent is initialized!"

    async def _init_mcp_manager(self):
        if not self.agent:
            return "Agent is not initialized properly."
        self.exit_stack = AsyncExitStack()
        await self.exit_stack.enter_async_context(self.agent.run_mcp_servers())

        return "Agent is ready!"

    async def _simple_chat(self, user_message, chat_history):
        bot_reply = await self.agent.run(
            user_message,
            chat_history=chat_history,
        )

        return bot_reply.output

    def _on_file_upload(self, file):
        if file:
            # gr.Success(f"File '{file.name}' uploaded successfully!")
            os.environ["OPENAPI_FILE"] = file.name
            return f"You uploaded: {file.name}"
        else:
            return "No file uploaded."

    async def _start_web(self):
        with gr.Blocks(title="OpenAPI Chatbot") as demo:
            with gr.Row():
                with gr.Sidebar():
                    file_input = gr.File(
                        label="Choose your OpenAPI yaml file",
                        file_types=[".yaml", ".yml"],
                        interactive=True,
                    )
                    status_output = gr.Textbox(label="Status", interactive=False)

                    file_input.change(
                        fn=self._on_file_upload,
                        inputs=file_input,
                        outputs=status_output,
                    ).then(
                        fn=self._init_agent,
                        inputs=[],
                        outputs=status_output,
                    ).then(
                        fn=self._init_mcp_manager,
                        inputs=[],
                        outputs=status_output,
                    )
                with gr.Column():
                    gr.ChatInterface(
                        fn=self._simple_chat,
                        type="messages",
                        theme="default",
                    )

        demo.launch()

    async def _start_cmd(self):
        yaml_file = input(
            "Enter the path to your OpenAPI yaml file [Default: openapi.yaml]: "
        ) or os.getenv("OPENAPI_FILE")
        if not yaml_file:
            raise ValueError("No OpenAPI yaml file provided.")
        os.environ["OPENAPI_FILE"] = yaml_file
        agent_status = await self._init_agent()
        if "ready" not in agent_status:
            print(agent_status)
            return
        async with self.agent.run_mcp_servers():
            chat_history = []
            while True:
                user_message = input("You: ")
                if user_message.lower() in ["exit", "quit"]:
                    print("Exiting chat...")
                    break
                bot_reply = await self._simple_chat(user_message, chat_history)
                print("Bot:", bot_reply)
