from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP, MCPServerStdio
from api_mcp import server
import gradio as gr
import uvicorn
import os


def get_sse_server(host=server.default_host, port=server.default_port):
    return MCPServerHTTP(
        url=f"http://{host}:{port}/sse")


def get_stdio_server():
    return MCPServerStdio(
        command="uv",
        args=["run", "server_exec.py"],)


class Chatbot:
    def __init__(self, use_sse: bool = False):
        if use_sse:
            mcp_server = get_sse_server()
        else:
            mcp_server = get_stdio_server()
        self.agent = Agent(
            os.getenv("MODEL", "openai:gpt-4o-mini"), mcp_servers=[mcp_server])

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

    async def start_web(self):
        with gr.Blocks(title="OpenAPI Chatbot") as demo:
            with gr.Row():
                with gr.Column(scale=1):
                    file_input = gr.File(label="Upload a file")
                    file_status = gr.Textbox(
                        label="File status", interactive=False)
                    file_input.change(self._on_file_upload,
                                      inputs=file_input, outputs=file_status)
                with gr.Column(scale=3):
                    chatbot = gr.ChatInterface(
                        fn=self._simple_chat,
                        type="messages",
                        theme="default",
                    )
        app, _, _ = demo.launch(prevent_thread_lock=True)

        async with self.agent.run_mcp_servers():
            config = uvicorn.Config(app, host="localhost", port=7865)
            server = uvicorn.Server(config)
            await server.serve()

    async def start_cmd(self):

        async with self.agent.run_mcp_servers():
            chat_history = []
            while True:
                user_message = input("You: ")
                if user_message.lower() in ["exit", "quit"]:
                    server.shutdown_event.set()
                    print("Exiting chat...")
                    break
                bot_reply = await self._simple_chat(user_message, chat_history)
                print("Bot:", bot_reply)
