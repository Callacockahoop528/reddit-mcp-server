"""Inbound (driving) adapter base — the contract all inbound adapters fulfil."""


class InboundAdapter:
    """Base class for all inbound (driving) adapters.

    Inbound adapters sit at the outer edge of the hexagon and *drive*
    the application by calling use-case / service methods.  Examples
    include CLI entry-points and MCP tool registrars.

    This is a marker base class for the type hierarchy; concrete
    abstract methods are defined in direct subclasses such as
    ``McpToolRegistrar``.
    """
