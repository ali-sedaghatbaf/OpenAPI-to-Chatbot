# from api_mcp.client import run_sse, run_stdio
from api_mcp import server
from api_gen.generator import generate_api
import asyncio
import importlib
import pkgutil
import api_code  # Import the generated API code
import os


def import_all_tool_modules(pkg):
    for _, module_name, is_pkg in pkgutil.iter_modules(pkg.__path__):
        if not is_pkg:
            importlib.import_module(f"{pkg.__name__}.{module_name}")


async def main():
    generate_api()
    import_all_tool_modules(api_code)
    use_sse = os.getenv("TRANSPORT") == "sse"
    await server.run(use_sse=use_sse)


if __name__ == "__main__":
    asyncio.run(main())
