from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime
from app.config import SECRET_KEY

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Dummy user database
users_db = {"user1": "password1"}

def create_access_token(username: str):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    return jwt.encode({"sub": username, "exp": expiration}, SECRET_KEY, algorithm="HS256")

async def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate user and return access token."""
    user = users_db.get(form_data.username)
    if not user or user != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"access_token": create_access_token(form_data.username), "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Decode and verify JWT token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
