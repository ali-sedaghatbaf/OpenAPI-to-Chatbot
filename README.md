# 🧠 OpenAPI to Chatbot

Build a fully functional **AI chatbot** that interacts with **any OpenAPI specification** automatically.

This project connects an LLM (like GPT-4o) to OpenAPI-documented APIs by turning OpenAPI endpoints into an **MCP server** (Message Control Protocol) that the chatbot can understand and call.

> Upload your OpenAPI YAML → Generate a ready-to-use AI assistant → Talk to your API!

---

## ✨ Features

- 📜 Parses any **OpenAPI** YAML specification
- ⚡️ Automatically spins up an **MCP** server to handle API calls
- 🤖 Uses a **Pydantic AI Agent** to chat intelligently with the API
- 🌐 Supports both **Web UI (Gradio)** and **Command Line (CMD)** interfaces
- 🔌 Flexible **transport options**: `stdio` or `sse`

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/ali-sedaghatbaf/OpenAPI-to-Chatbot.git
cd OpenAPI-to-Chatbot
uv sync
```

Copy .encv.example into a.env file and initialize the variables properly.
OPENAPI_FILE=         # Path to your OpenAPI YAML (optional at startup)
AI_MODEL=gpt-4o       # Your model name (e.g., gpt-4, gpt-4o, etc.)
TRANSPORT=stdio       # 'stdio' or 'sse'
CHAT_UI=web           # 'web' for Gradio or 'cmd' for terminal
MCP_HOST=127.0.0.1    # (Only for 'sse' mode)
MCP_PORT=8000         # (Only for 'sse' mode)

🚀 Running the App
uv run main.py

🧠 How It Works

1. Upload an OpenAPI specification (YAML format).

2. The app dynamically spins up a local MCP server based on the OpenAPI endpoints.

3. A Pydantic AI Agent loads and connects to the MCP server.

4. Chat naturally with your API — the agent maps your requests into API calls!

