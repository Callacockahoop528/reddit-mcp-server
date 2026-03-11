"""Port interfaces — contracts between application and infrastructure."""

from reddit_mcp_server.ports.config import ConfigPort
from reddit_mcp_server.ports.inbound import InboundAdapter
from reddit_mcp_server.ports.outbound import OutboundAdapter
from reddit_mcp_server.ports.reddit import RedditPort

__all__ = [
    "ConfigPort",
    "InboundAdapter",
    "OutboundAdapter",
    "RedditPort",
]
