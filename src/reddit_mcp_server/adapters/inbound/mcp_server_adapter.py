"""MCP server adapter — creates and configures the FastMCP server instance."""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastmcp import FastMCP

from reddit_mcp_server.adapters.inbound.mcp_tools import (
    McpPostToolRegistrar,
    McpSearchToolRegistrar,
    McpUserToolRegistrar,
)
from reddit_mcp_server.container import Container
from reddit_mcp_server.ports.inbound import InboundAdapter

logger = logging.getLogger(__name__)


class McpServerAdapter(InboundAdapter):
    """Inbound adapter that creates and runs the FastMCP server.

    Wires tool registrars to the MCP server and manages its lifecycle.
    """

    def __init__(self, container: Container) -> None:
        self._container = container

    def create(self) -> FastMCP:
        """Create a configured FastMCP server with all tools registered."""
        container = self._container

        @asynccontextmanager
        async def server_lifespan(app: FastMCP) -> AsyncIterator[dict]:
            logger.info("Reddit MCP Server starting...")
            yield {}
            logger.info("Reddit MCP Server shutting down...")
            await container.reddit.close()

        mcp = FastMCP(
            "reddit_mcp_server",
            lifespan=server_lifespan,
        )

        # Register all tools via class-based registrars
        registrars = [
            McpPostToolRegistrar(container.post_service),
            McpSearchToolRegistrar(container.search_service),
            McpUserToolRegistrar(container.user_service),
        ]
        for registrar in registrars:
            registrar.register(mcp)

        return mcp
