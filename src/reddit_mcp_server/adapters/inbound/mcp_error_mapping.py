"""Domain exception → MCP ToolError mapping.

This is the ONLY file that imports from fastmcp.exceptions.
All redd/domain errors are translated to user-friendly ToolError messages here.
"""

import logging
from typing import NoReturn

from fastmcp.exceptions import ToolError
from redd import HttpError, NotFoundError, ParseError, ReddError

from reddit_mcp_server.domain.exceptions import (
    ConfigurationError,
    RedditMCPError,
)

logger = logging.getLogger(__name__)


class McpErrorMapper:
    """Maps domain and redd exceptions to MCP ``ToolError`` responses.

    Centralises error translation so that MCP tool handlers never need
    to import ``fastmcp.exceptions`` directly.
    """

    @staticmethod
    def map(exception: Exception, context: str = "") -> NoReturn:
        """Map domain/redd exceptions to ToolError for MCP clients.

        Args:
            exception: The caught exception.
            context: Optional context string (e.g. tool name).

        Raises:
            ToolError: Always, with a user-friendly message.
        """
        prefix = f"[{context}] " if context else ""

        if isinstance(exception, NotFoundError):
            raise ToolError(
                f"{prefix}Resource not found. Please check the username, subreddit, or permalink."
            ) from exception

        if isinstance(exception, HttpError):
            raise ToolError(
                f"{prefix}HTTP error ({exception.status_code}). "
                "Reddit may be temporarily unavailable. Please try again later."
            ) from exception

        if isinstance(exception, ParseError):
            raise ToolError(
                f"{prefix}Failed to parse Reddit response. The data format may have changed."
            ) from exception

        if isinstance(exception, ReddError):
            raise ToolError(f"{prefix}{exception}") from exception

        if isinstance(exception, ConfigurationError):
            raise ToolError(f"{prefix}Configuration error: {exception}") from exception

        if isinstance(exception, RedditMCPError):
            raise ToolError(f"{prefix}{exception}") from exception

        # Unknown exception — log and re-raise with masked details
        logger.exception("Unexpected error in %s", context or "unknown context")
        raise ToolError(
            f"{prefix}An unexpected error occurred. Check server logs for details."
        ) from exception
