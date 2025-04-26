from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP, MCPServerStdio
import inspect
from api_mcp import client
import gradio as gr
import uvicorn
import os


class Chatbot:

    async def start(self):
        await self._init_agent()

        use_web = os.getenv("CHAT_UI") == "web"
        if use_web:
            await self._start_web()
        else:
            await self._start_cmd()

    async def _init_agent(self):
        use_sse = os.getenv("TRANSPORT") == "sse"
        if use_sse:
            host = os.getenv("MCP_HOST")
            port = int(os.getenv("MCP_PORT"))
            mcp_server = MCPServerHTTP(url=f"http://{host}:{port}/sse")
        else:
            mcp_server = MCPServerStdio(command="uv",
                                        args=["run", "server_exec.py"],)

        self.agent = Agent(
            os.getenv("AI_MODEL"), mcp_servers=[mcp_server], verbose=True)

    async def _simple_chat(self, user_message, chat_history):

        bot_reply = await self.agent.run(
            user_message,
            chat_history=chat_history,
        )

        return bot_reply.output

    def _on_file_upload(self, file):
        if file:
            gr.success(f"File '{file.name}' uploaded successfully!")
            return f"You uploaded: {file.name}"
        else:
            return "No file uploaded."

    async def _start_web(self):
        with gr.Blocks(title="OpenAPI Chatbot") as demo:
            with gr.Row():
                with gr.Column(scale=1):
                    pass
                with gr.Column(scale=3):
                    chatbot = gr.ChatInterface(
                        fn=self._simple_chat,
                        type="messages",
                        theme="default",
                    )
                with gr.Column(scale=1):
                    pass
        app, _, _ = demo.launch(prevent_thread_lock=True)

        async with self.agent.run_mcp_servers():
            config = uvicorn.Config(app, host="localhost", port=7865)
            server = uvicorn.Server(config)
            await server.serve()

    async def _start_cmd(self):

        async with self.agent.run_mcp_servers():
            chat_history = []
            while True:
                user_message = input("You: ")
                if user_message.lower() in ["exit", "quit"]:

                    print("Exiting chat...")
                    break
                bot_reply = await self._simple_chat(user_message, chat_history)
                print("Bot:", bot_reply)
