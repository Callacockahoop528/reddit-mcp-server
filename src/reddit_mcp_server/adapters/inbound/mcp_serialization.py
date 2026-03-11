"""MCP serialization utilities for converting redd domain models to JSON-serializable dicts."""

from dataclasses import asdict
from typing import Any


class McpSerializer:
    """Serializes redd domain models into JSON-compatible dictionaries.

    Provides helper methods to convert frozen dataclasses into plain
    dicts suitable for MCP tool responses.
    """

    @staticmethod
    def serialize(model: object) -> dict[str, Any]:
        """Convert a frozen dataclass to a JSON-serializable dict, stripping None values."""
        return {k: v for k, v in asdict(model).items() if v is not None}  # type: ignore[arg-type]

    @staticmethod
    def serialize_list(models: list) -> list[dict[str, Any]]:
        """Serialize a list of dataclass models."""
        return [McpSerializer.serialize(m) for m in models]
