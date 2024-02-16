

import redis.asyncio as redis

from src.core.settings import load_setting


async def connect_redis() -> redis.Redis:
    client = redis.from_url(load_setting().redis_setting.get_url)
    async with client:
        yield client
