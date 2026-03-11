"""Immutable value objects for configuration."""

from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class ServerConfig:
    """MCP server configuration values."""

    transport: Literal["stdio", "streamable-http"] = "stdio"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "WARNING"
    host: str = "127.0.0.1"
    port: int = 8000
    path: str = "/mcp"


@dataclass(frozen=True)
class RedditConfig:
    """Reddit client configuration values."""

    proxy: str | None = None
    timeout: float = 10.0
    throttle_min: float = 1.0
    throttle_max: float = 2.0


@dataclass(frozen=True)
class AppConfig:
    """Complete application configuration."""

    server: ServerConfig = ServerConfig()  # type: ignore[call-arg]
    reddit: RedditConfig = RedditConfig()  # type: ignore[call-arg]
