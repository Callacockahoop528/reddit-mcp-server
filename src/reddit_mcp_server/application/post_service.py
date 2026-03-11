"""Post service — post-related application operations."""

from redd.domain.enums import Category, TimeFilter
from redd.domain.models import PostDetail, SubredditPost

from reddit_mcp_server.ports.reddit import RedditPort


class PostService:
    """Application service for post-related operations.

    Groups ``get_post`` and ``get_subreddit_posts`` under a single
    cohesive class that depends only on the ``RedditPort`` abstraction.
    """

    def __init__(self, reddit: RedditPort) -> None:
        self._reddit = reddit

    async def get_post(self, permalink: str) -> PostDetail:
        """Get full post details including its comment tree."""
        return await self._reddit.get_post(permalink)

    async def get_subreddit_posts(
        self,
        subreddit: str,
        *,
        limit: int = 25,
        category: str | None = None,
        time_filter: str | None = None,
    ) -> list[SubredditPost]:
        """Fetch posts from a subreddit listing (hot, top, new, rising)."""
        cat = Category(category) if category else Category.HOT
        tf = TimeFilter(time_filter) if time_filter else TimeFilter.ALL
        return await self._reddit.get_subreddit_posts(
            subreddit, limit=limit, category=cat, time_filter=tf
        )
