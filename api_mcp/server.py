import sys
from mcp.server.fastmcp import FastMCP
import asyncio
import logging
import os
import dotenv

dotenv.load_dotenv(override=True)
logger = logging.getLogger(__name__)

mcp_server = FastMCP("API Server", host=os.getenv(
    "MCP_HOST"), port=os.getenv("MCP_PORT"))


async def run_stdio():

    print("Starting STDIO MCP server...", flush=True)
    await mcp_server.run_stdio_async()


async def run_sse():

    print(f"Starting SSE MCP Server...", flush=True)

    await mcp_server.run_sse_async()
