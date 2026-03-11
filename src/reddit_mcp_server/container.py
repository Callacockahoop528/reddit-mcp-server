"""Dependency Injection container — the composition root.

This is the single place where ports are wired to adapter implementations
and services are assembled. Only this file imports concrete adapter classes.
"""

from reddit_mcp_server.adapters.outbound.redd_reddit_adapter import ReddRedditAdapter
from reddit_mcp_server.application.post_service import PostService
from reddit_mcp_server.application.search_service import SearchService
from reddit_mcp_server.application.user_service import UserService
from reddit_mcp_server.domain.value_objects import AppConfig
from reddit_mcp_server.ports.reddit import RedditPort


class Container:
    """Dependency Injection container.

    Wires ports to adapters and creates service instances.
    This is the only place in the codebase where concrete adapter
    classes are imported and instantiated.
    """

    def __init__(self, config: AppConfig) -> None:
        self._config = config

        # Outbound adapters
        self._reddit: RedditPort = ReddRedditAdapter(config.reddit)

        # Application services
        self._post_service = PostService(self._reddit)
        self._user_service = UserService(self._reddit)
        self._search_service = SearchService(self._reddit)

    @property
    def config(self) -> AppConfig:
        return self._config

    @property
    def reddit(self) -> RedditPort:
        return self._reddit

    @property
    def post_service(self) -> PostService:
        return self._post_service

    @property
    def user_service(self) -> UserService:
        return self._user_service

    @property
    def search_service(self) -> SearchService:
        return self._search_service
