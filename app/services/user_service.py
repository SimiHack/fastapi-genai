from app.auth import create_access_token

async def login_user(username: str, password: str):
    return {"access_token": create_access_token(username), "token_type": "bearer"}

