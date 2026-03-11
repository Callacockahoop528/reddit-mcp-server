"""Reddit port — abstracts all Reddit data access."""

from abc import abstractmethod

from redd.domain.enums import Category, SortOrder, TimeFilter, UserCategory
from redd.domain.models import PostDetail, SearchResult, SubredditPost, UserItem

from reddit_mcp_server.ports.outbound import OutboundAdapter


class RedditPort(OutboundAdapter):
    """Port for Reddit data extraction.

    Extends OutboundAdapter so every concrete implementation inherits
    the ``close()`` contract.  Abstracts the underlying HTTP client so
    the application layer never depends on a concrete scraping implementation.
    """

    @abstractmethod
    async def search(
        self,
        query: str,
        *,
        limit: int = 25,
        sort: SortOrder = SortOrder.RELEVANCE,
    ) -> list[SearchResult]:
        """Search all of Reddit for posts matching *query*."""
        ...

    @abstractmethod
    async def search_subreddit(
        self,
        subreddit: str,
        query: str,
        *,
        limit: int = 25,
        sort: SortOrder = SortOrder.RELEVANCE,
    ) -> list[SearchResult]:
        """Search within a specific subreddit."""
        ...

    @abstractmethod
    async def get_post(self, permalink: str) -> PostDetail:
        """Get full post details including comment tree."""
        ...

    @abstractmethod
    async def get_user(self, username: str, *, limit: int = 25) -> list[UserItem]:
        """Get a user's recent public activity."""
        ...

    @abstractmethod
    async def get_subreddit_posts(
        self,
        subreddit: str,
        *,
        limit: int = 25,
        category: Category = Category.HOT,
        time_filter: TimeFilter = TimeFilter.ALL,
    ) -> list[SubredditPost]:
        """Fetch posts from a subreddit listing."""
        ...

    @abstractmethod
    async def get_user_posts(
        self,
        username: str,
        *,
        limit: int = 25,
        category: UserCategory = UserCategory.NEW,
        time_filter: TimeFilter = TimeFilter.ALL,
    ) -> list[SubredditPost]:
        """Fetch a user's submitted posts."""
        ...

    @abstractmethod
    async def close(self) -> None:
        """Release underlying resources."""
        ...
