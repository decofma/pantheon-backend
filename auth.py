from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from passlib.context import CryptContext
from models import Token, TokenData, User, UserCreate, UserInDB
from database import users_collection

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    user = users_collection.find_one({"username": username})
    if user:
        return UserInDB(username=user["username"], hashed_password=user["hashed_password"])
    return None

def create_access_token(data: dict, secret_key: str, algorithm: str, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)

def authenticate_user(username: str, password: str, secret_key: str, algorithm: str, expire_minutes: int):
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=expire_minutes)
    access_token = create_access_token(data={"sub": user.username}, secret_key=secret_key, algorithm=algorithm, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

def register_user(user_create: UserCreate, secret_key: str, algorithm: str, expire_minutes: int):
    if get_user(user_create.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = get_password_hash(user_create.password)
    users_collection.insert_one({"username": user_create.username, "hashed_password": hashed})
    access_token_expires = timedelta(minutes=expire_minutes)
    access_token = create_access_token(data={"sub": user_create.username}, secret_key=secret_key, algorithm=algorithm, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str, secret_key: str, algorithm: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user
