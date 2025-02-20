from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str
    password: str

class Move(BaseModel):
    move_type: str
    data: dict

class GameState(BaseModel):
    game_id: str
    players: List[str]
    turn: str
    life_points: Dict[str, int]
    faith_points: Dict[str, int]
    hand: Dict[str, List[Any]]
    deck: Dict[str, List[Any]]
    field: Dict[str, List[Any]]
    log: List[str]
