import os
from dotenv import load_dotenv

load_dotenv()
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
REDIS_URL = os.getenv("REDIS_URL")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_URL}"
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE", "openai")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL.startswith("postgresql://"):
	DATABASE_URL = f"postgresql://{DATABASE_URL}"

print(f"Databse URL: {DATABASE_URL}")