from api_mcp import client, server, chat
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":

    run_mode = os.getenv("MODE", "chat")
    if run_mode == "chat":
        chatbot = chat.Chatbot(use_sse=os.getenv(
            "TRANSPORT") == "sse")
        if os.getenv("UI") == "web":
            asyncio.run(chatbot.start_web())
        else:
            asyncio.run(chatbot.start_cmd())
    else:
        if os.getenv("TRANSPORT") == "sse":
            asyncio.run(client.run_sse())
        else:
            asyncio.run(client.run_stdio())
