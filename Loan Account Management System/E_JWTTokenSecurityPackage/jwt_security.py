from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

SECRET_KEY = "SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def create_access_token(token_data: dict):
    to_encode = token_data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expires})
    jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_token

def password_hash(user_password):
    pass_key = pwd_context.hash(user_password)
    return pass_key

def verify_password(user_password, hashed_password):
    pass_key = pwd_context.verify(user_password, hashed_password)
    return pass_key

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_username = payload.get("user_username")
        if user_username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return user_username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)