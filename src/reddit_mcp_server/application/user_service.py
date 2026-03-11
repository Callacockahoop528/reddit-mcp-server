"""User service — user-related application operations."""

from redd.domain.enums import TimeFilter, UserCategory
from redd.domain.models import SubredditPost, UserItem

from reddit_mcp_server.ports.reddit import RedditPort


class UserService:
    """Application service for user-related operations.

    Groups ``get_user`` and ``get_user_posts`` under a single
    cohesive class that depends only on the ``RedditPort`` abstraction.
    """

    def __init__(self, reddit: RedditPort) -> None:
        self._reddit = reddit

    async def get_user(self, username: str, *, limit: int = 25) -> list[UserItem]:
        """Get a user's recent public activity feed."""
        return await self._reddit.get_user(username, limit=limit)

    async def get_user_posts(
        self,
        username: str,
        *,
        limit: int = 25,
        category: str | None = None,
        time_filter: str | None = None,
    ) -> list[SubredditPost]:
        """Fetch a user's submitted posts."""
        cat = UserCategory(category) if category else UserCategory.NEW
        tf = TimeFilter(time_filter) if time_filter else TimeFilter.ALL
        return await self._reddit.get_user_posts(
            username, limit=limit, category=cat, time_filter=tf
        )
