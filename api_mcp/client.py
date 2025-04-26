from mcp import types, StdioServerParameters
from mcp.client.sse import sse_client
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from api_mcp import server
from pathlib import Path
import sys
import os
from pydantic_ai import Tool
import inspect
# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="uv",
    args=["run", "server_exec.py"],
    log_output=True,
)


# Optional: create a sampling callback
async def handle_sampling_message(
    message: types.CreateMessageRequestParams,
) -> types.CreateMessageResult:
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="Hello, world! from model",
        ),
        model="gpt-3.5-turbo",
        stopReason="endTurn",
    )


async def run_sse():
    host = os.getenv("MCP_HOST")
    port = int(os.getenv("MCP_PORT"))
    async with sse_client(f"http://{host}:{port}/sse") as streams:

        async with ClientSession(streams[0], streams[1], sampling_callback=handle_sampling_message) as session:
            await run_session(session)


async def run_stdio():
    async with stdio_client(server_params, errlog=sys.stdout) as streams:
        async with ClientSession(streams[0], streams[1]) as session:
            await run_session(session)


async def run_session(session: ClientSession):

    # Initialize the connection
    initialization_result = await session.initialize()
    print(f"Connected to {initialization_result.serverInfo.name}")
    # List available prompts
    # prompts = await session.list_prompts()

    # Get a prompt
    # prompt = await session.get_prompt(
    #    "example-prompt", arguments={"arg1": "value"}
    # )

    # List available resources
    # resources = await session.list_resources()

    # List available tools
    response = await session.list_tools()

    print(f"Available tools: {[tool.name for tool in response.tools]}")
    # Call a tool
    # result = await session.call_tool("pet_get_find_pets_by_status", arguments={"params": {"status": "sold"}})
    # print(result.content)
