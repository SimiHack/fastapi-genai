import redis.asyncio as redis
from app.config import REDIS_URL

# Correctly parse the REDIS_URL to extract host and port
redis_url = REDIS_URL.replace("rediss://", "").replace("redis://", "")
redis_url_parts = redis_url.split("@")
host_port = redis_url_parts[1].split(":")
host = host_port[0]
port = int(host_port[1])

redis_client = redis.RedisCluster(
    host=host,
    port=port,
    password=redis_url_parts[0].split(":")[1],
    decode_responses=True
)

async def execute_redis_command(command, *args, **kwargs):
    try:
        return await redis_client.execute_command(command, *args, **kwargs)
    except redis.exceptions.ResponseError as e:
        if "MOVED" in str(e):
            # Handle MOVED response error
            return await redis_client.execute_command(command, *args, **kwargs)
        raise e

async def close_redis_client():
    await redis_client.close()
