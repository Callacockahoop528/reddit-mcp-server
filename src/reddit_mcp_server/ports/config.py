"""Config port — abstracts configuration loading."""

from abc import abstractmethod

from reddit_mcp_server.domain.value_objects import AppConfig
from reddit_mcp_server.ports.outbound import OutboundAdapter


class ConfigPort(OutboundAdapter):
    """Port for configuration loading and access.

    Extends OutboundAdapter to participate in the adapter hierarchy.
    Config adapters typically hold no resources, so ``close()`` is a no-op
    unless overridden.
    """

    @abstractmethod
    def load(self) -> AppConfig:
        """Load and return the complete application configuration.

        Implementations should handle:
        - Default values
        - Environment variables
        - CLI arguments
        - .env files

        Returns an immutable AppConfig.
        """
        ...

    async def close(self) -> None:
        """Config adapters typically hold no resources."""
