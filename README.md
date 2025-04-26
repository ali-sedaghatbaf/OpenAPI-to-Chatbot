# 🛠️ OpenAPI-to-Chatbot

This project (still WIP) reads an **OpenAPI spec** (in YAML format), automatically generates a **FastAPI** app from it, wraps the app with an **MCP server**, and uses **pydantic_ai Agents** to enable **conversational interaction** with the API — as if the user is "talking" to the API.

---

## ✨ Features

- 📝 Load OpenAPI 3.0 spec from a `.yaml` file
- ⚡ Generate FastAPI routes dynamically
- 🔌 Expose the API over MCP (Message Control Protocol)
- 🤖 Power natural language conversations with `pydantic_ai.Agent`
- 🎯 Seamlessly connect the user to any OpenAPI-described backend

## 🚀 How It Works
1. Load the OpenAPI YAML
Parse the OpenAPI file and dynamically build matching FastAPI endpoints.

2. Wrap with MCP Server
Use FastMCP to expose the API for machine-to-machine or agent interaction.

3. Enable Chat with pydantic_ai Agent
Spin up an agent that reads the OpenAPI description and lets users "talk" to the API in natural language.
