"""Search service — search-related application operations."""

from redd.domain.enums import SortOrder
from redd.domain.models import SearchResult

from reddit_mcp_server.ports.reddit import RedditPort


class SearchService:
    """Application service for search-related operations.

    Groups ``search`` and ``search_subreddit`` under a single
    cohesive class that depends only on the ``RedditPort`` abstraction.
    """

    def __init__(self, reddit: RedditPort) -> None:
        self._reddit = reddit

    async def search(
        self,
        query: str,
        *,
        limit: int = 25,
        sort: str | None = None,
    ) -> list[SearchResult]:
        """Search all of Reddit for posts matching a query."""
        sort_order = SortOrder(sort) if sort else SortOrder.RELEVANCE
        return await self._reddit.search(query, limit=limit, sort=sort_order)

    async def search_subreddit(
        self,
        subreddit: str,
        query: str,
        *,
        limit: int = 25,
        sort: str | None = None,
    ) -> list[SearchResult]:
        """Search within a specific subreddit."""
        sort_order = SortOrder(sort) if sort else SortOrder.RELEVANCE
        return await self._reddit.search_subreddit(subreddit, query, limit=limit, sort=sort_order)
