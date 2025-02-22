from redis.asyncio import RedisCluster
from app.config import REDIS_URL

async def get_redis():
    redis_client = await RedisCluster.from_url(REDIS_URL, decode_responses=True, ssl=True)
    return redis_client
