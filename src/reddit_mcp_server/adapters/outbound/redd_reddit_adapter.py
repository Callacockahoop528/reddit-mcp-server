"""Redd Reddit adapter — RedditPort implementation.

Wraps the async redd client (AsyncRedd) behind the RedditPort interface.
"""

from redd import AsyncRedd
from redd.domain.enums import Category, SortOrder, TimeFilter, UserCategory
from redd.domain.models import PostDetail, SearchResult, SubredditPost, UserItem

from reddit_mcp_server.domain.value_objects import RedditConfig
from reddit_mcp_server.ports.reddit import RedditPort


class ReddRedditAdapter(RedditPort):
    """RedditPort implementation backed by redd's AsyncRedd client.

    Naming convention: ``Redd`` (implementation) + ``Reddit`` (port) + ``Adapter``.
    """

    def __init__(self, config: RedditConfig) -> None:
        super().__init__()
        self._client = AsyncRedd(
            proxy=config.proxy,
            timeout=config.timeout,
            throttle=(config.throttle_min, config.throttle_max),
        )

    async def search(
        self,
        query: str,
        *,
        limit: int = 25,
        sort: SortOrder = SortOrder.RELEVANCE,
    ) -> list[SearchResult]:
        return await self._client.search(query, limit=limit, sort=sort)

    async def search_subreddit(
        self,
        subreddit: str,
        query: str,
        *,
        limit: int = 25,
        sort: SortOrder = SortOrder.RELEVANCE,
    ) -> list[SearchResult]:
        return await self._client.search_subreddit(subreddit, query, limit=limit, sort=sort)

    async def get_post(self, permalink: str) -> PostDetail:
        return await self._client.get_post(permalink)

    async def get_user(self, username: str, *, limit: int = 25) -> list[UserItem]:
        return await self._client.get_user(username, limit=limit)

    async def get_subreddit_posts(
        self,
        subreddit: str,
        *,
        limit: int = 25,
        category: Category = Category.HOT,
        time_filter: TimeFilter = TimeFilter.ALL,
    ) -> list[SubredditPost]:
        return await self._client.get_subreddit_posts(
            subreddit, limit=limit, category=category, time_filter=time_filter
        )

    async def get_user_posts(
        self,
        username: str,
        *,
        limit: int = 25,
        category: UserCategory = UserCategory.NEW,
        time_filter: TimeFilter = TimeFilter.ALL,
    ) -> list[SubredditPost]:
        return await self._client.get_user_posts(
            username, limit=limit, category=category, time_filter=time_filter
        )

    async def close(self) -> None:
        await self._client.close()
