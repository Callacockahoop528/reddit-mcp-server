"""MCP tool registrations."""

from reddit_mcp_server.adapters.inbound.mcp_tools._base import McpToolRegistrar
from reddit_mcp_server.adapters.inbound.mcp_tools.mcp_post_tools import McpPostToolRegistrar
from reddit_mcp_server.adapters.inbound.mcp_tools.mcp_search_tools import McpSearchToolRegistrar
from reddit_mcp_server.adapters.inbound.mcp_tools.mcp_user_tools import McpUserToolRegistrar

__all__ = [
    "McpPostToolRegistrar",
    "McpSearchToolRegistrar",
    "McpToolRegistrar",
    "McpUserToolRegistrar",
]
