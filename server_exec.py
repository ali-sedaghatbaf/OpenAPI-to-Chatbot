# from api_mcp.client import run_sse, run_stdio
from api_mcp import server
from api_gen.generator import generate_api
import asyncio
import importlib
import pkgutil
import api_tools  # Import the generated API code
import os
import sys


def import_all_tool_modules(pkg):
    for _, module_name, is_pkg in pkgutil.iter_modules(pkg.__path__):
        if not is_pkg:
            importlib.import_module(f"{pkg.__name__}.{module_name}")


async def main():
    generate_api()
    import_all_tool_modules(api_tools)
    use_sse = os.getenv("TRANSPORT") == "sse"

    if use_sse:
        await server.run_sse()
    else:
        await server.run_stdio()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")

        exit(0)
