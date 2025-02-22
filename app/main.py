from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.routes import chat, health
from app.auth import authenticate_user

app = FastAPI()

app.include_router(chat.router, prefix="/api", tags=["Chat"])
app.include_router(health.router, prefix="/api", tags=["Health"])

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await authenticate_user(form_data)

@app.get("/")
async def root():
    return {"message": "GenAI FastAPI service running with Authentication, Caching & DB!"}
