import asyncpg
from app.config import DATABASE_URL
import logging

# Configure logging to output to the terminal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

async def get_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        logging.info("Database connection established")
        return conn
    except asyncpg.exceptions.ConnectionDoesNotExistError:
        logging.error("Database connection does not exist.")
    except asyncpg.exceptions.InvalidCatalogNameError:
        logging.error("Database does not exist.")
    except asyncpg.exceptions.InvalidPasswordError:
        logging.error("Invalid password.")
    except asyncpg.exceptions.CannotConnectNowError:
        logging.error("Cannot connect to the database now.")
    except Exception as e:
        logging.error(f"Failed to get database connection: {e}")
    return None
