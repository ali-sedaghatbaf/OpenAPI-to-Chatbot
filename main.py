import asyncio
from dotenv import load_dotenv

load_dotenv(".env", override=True)


if __name__ == "__main__":
    from api_mcp import chat, errors

    try:
        chatbot = chat.Chatbot()
        asyncio.run(chatbot.start())

    except errors.MCPError as e:
        print(f"Error communicating with the MCP Server: {e}")

        exit(1)
    except ValueError as e:
        print(f"Error: {e}")

        exit(1)
    except KeyboardInterrupt:
        print("Shutting down...")

        exit(0)
