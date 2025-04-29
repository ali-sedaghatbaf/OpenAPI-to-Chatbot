from mcp.server.fastmcp import FastMCP
import logging
import os
import dotenv

dotenv.load_dotenv(override=True)
logger = logging.getLogger(__name__)


class MCPServer:
    _singleton_instance: "MCPServer" = None

    def __init__(self):
        # Configuration
        self.use_sse = os.getenv("TRANSPORT") == "sse"
        self.host = os.getenv("MCP_HOST")
        self.port = int(os.getenv("MCP_PORT", 0)) if os.getenv("MCP_PORT") else None
        self.name = "API-MCP-Server"

        # Actual MCP server instance
        self._server = None

    @property
    def server(self) -> FastMCP:
        if self._server is None:
            if self.use_sse:
                self._server = FastMCP(
                    host=self.host,
                    port=self.port,
                    name=self.name,
                )
            else:
                self._server = FastMCP(
                    name=self.name,
                )
        return self._server

    async def run_async(self):
        if self.use_sse:
            await self.server.run_sse_async()
        else:
            await self.server.run_stdio_async()

    @classmethod
    def get_instance(cls) -> "MCPServer":
        if cls._singleton_instance is None:
            cls._singleton_instance = MCPServer()
        return cls._singleton_instance


mcp_server = MCPServer.get_instance().server


async def run_async_server():
    await MCPServer.get_instance().run_async()
