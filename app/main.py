from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.routes import chat, health
from app.auth import authenticate_user

app = FastAPI()

app.include_router(chat.router, tags=["Chat"])
app.include_router(health.router, tags=["Health"])

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await authenticate_user(form_data)
