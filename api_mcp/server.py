from mcp.server.fastmcp import FastMCP
import asyncio
import logging

logger = logging.getLogger(__name__)

default_host = "127.0.0.1"
default_port = 8001

mcp_server = FastMCP(
    name="API Server",
    host=default_host,
    port=default_port,
)
shutdown_event = asyncio.Event()


async def run_stdio():
    await mcp_server.run_stdio_async()


async def run_sse(host=default_host, port=default_port):
    mcp_server.host = host
    mcp_server.port = port
    await mcp_server.run_sse_async()


async def run(use_sse=False, host=default_host, port=default_port):
    if use_sse:
        run_task = asyncio.create_task(run_sse(host, port))
    else:
        run_task = asyncio.create_task(run_stdio())
    await shutdown_event.wait()
    run_task.cancel()
