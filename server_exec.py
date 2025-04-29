# from api_mcp.client import run_sse, run_stdio
from api_mcp.server import run_async_server
from api_gen.generator import generate_api
import asyncio
import importlib
import pkgutil
import api_tools
import os


def import_all_tool_modules(pkg):
    for _, module_name, is_pkg in pkgutil.iter_modules(pkg.__path__):
        if not is_pkg:
            importlib.import_module(f"{pkg.__name__}.{module_name}")


async def main():
    generate_api(input_path=os.getenv("OPENAPI_FILE"))
    import_all_tool_modules(api_tools)
    await run_async_server()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Shutting down...")

        exit(0)
