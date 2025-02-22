from fastapi import APIRouter, Depends, HTTPException
from app.models import ChatRequest, ChatResponse
from app.auth import get_current_user
from app.cache import get_redis
from app.db import get_db
from app.services.openai_service import generate_ai_response
from app.services.redis_service import close_redis_client
import logging

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@router.post("/generate", response_model=ChatResponse)
async def generate_text(request: ChatRequest, user: str = Depends(get_current_user)):
    redis_conn = await get_redis()
    db = None
    ai_response = None
    try:
        # 🔹 LOGGING BEFORE CHECKING CACHE
        logger.info(f"Received prompt: {request.prompt} from user: {user}")

        # 🔹 GET DATABASE CONNECTION
        db = await get_db()
        if db is None:
            logger.error("Database connection failed")
            raise HTTPException(status_code=500, detail="Database connection error")

        logger.info("Database connection established")

        # 🔹 CHECK CACHE FIRST (BUT FORCE A DATABASE INSERT)
        cached_response = await redis_conn.get(request.prompt)
        if cached_response:
            logger.info("Returning cached response, but inserting into DB as well")
        else:
            # 🔹 GENERATE AI RESPONSE
            ai_response = await generate_ai_response(request.prompt)

            # 🔹 STORE RESPONSE IN CACHE
            await redis_conn.setex(request.prompt, 3600, ai_response)

            # Use generated response instead of cached one
            cached_response = ai_response

        # 🔹 INSERT INTO DATABASE
        async with db.transaction():
            await db.execute(
                "INSERT INTO chat_history (user_id, prompt, response) VALUES ($1, $2, $3)",
                user, request.prompt, cached_response
            )
        logger.info("Insertion successful in chat_history table")

        return ChatResponse(response=cached_response, cached=(cached_response != ai_response))

    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in processing request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        try:
            if db:
                await db.close()
            if redis_conn:
                await redis_conn.close()
                logger.info("Redis connection closed successfully")
        except Exception as close_error:
            logger.error(f"Error closing connections: {close_error}", exc_info=True)
