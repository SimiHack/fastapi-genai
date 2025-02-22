import redis.asyncio as redis
from app.config import REDIS_URL, REDIS_PASSWORD

redis_client = redis.RedisCluster(
    host=REDIS_URL.split(":")[0],
    port=int(REDIS_URL.split(":")[1]),
    password=REDIS_PASSWORD,
    decode_responses=True
)

async def test_redis_connection():
    try:
        await redis_client.ping()
        print("Redis connection successful")
    except Exception as e:
        print(f"Redis connection failed: {e}")
