"""Base MCP tool registrar — abstract base for all MCP tool registration adapters."""

from abc import abstractmethod

from fastmcp import FastMCP

from reddit_mcp_server.ports.inbound import InboundAdapter


class McpToolRegistrar(InboundAdapter):
    """Base class for all MCP tool registrar adapters.

    Each concrete registrar groups related MCP tools (e.g. post tools,
    search tools) and registers them on a ``FastMCP`` server instance.

    Subclasses must implement :meth:`register` to declare their tools
    on the provided ``FastMCP`` instance.
    """

    @abstractmethod
    def register(self, mcp: FastMCP) -> None:
        """Register MCP tools on the given server instance."""
        ...
