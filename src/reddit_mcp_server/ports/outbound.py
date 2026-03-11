"""Outbound (driven) adapter base — the contract all outbound adapters fulfil."""

from abc import ABC, abstractmethod


class OutboundAdapter(ABC):
    """Base class for all outbound (driven) adapters.

    Outbound adapters implement port interfaces to provide infrastructure
    services (HTTP clients, config loaders, databases, etc.) to the
    application layer.  Every outbound adapter MUST be closeable so the
    composition root can release resources on shutdown.
    """

    @abstractmethod
    async def close(self) -> None:
        """Release underlying resources (connections, file handles, etc.)."""
        ...
