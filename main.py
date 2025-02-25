# backend/main.py
from fastapi import FastAPI, Depends, HTTPException, Body
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import uvicorn
import os
from cards import get_all_cards

from models import User, Move, MatchRoomRequest
import auth
import game

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

# Habilitar CORS (ajuste allow_origins conforme necessário)
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/auth/register")
def register(user: auth.UserCreate):
    return auth.register_user(user, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.authenticate_user(form_data.username, form_data.password, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

def get_current_user(token: str = Depends(auth.oauth2_scheme)):
    return auth.get_current_user(token, SECRET_KEY, ALGORITHM)

@app.post("/matchmaking/join")
def join_matchmaking(current_user: User = Depends(get_current_user)):
    game_state = game.join_matchmaking(current_user.username)
    return game_state

@app.get("/matchmaking/status")
def matchmaking_status(current_user: User = Depends(get_current_user)):
    status = game.get_matchmaking_status(current_user.username)
    return status

@app.post("/match/create")
def create_match_room_endpoint(request: MatchRoomRequest, current_user: User = Depends(get_current_user)):
    result = game.create_match_room(current_user.username, request.room_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/match/join")
def join_match_room_endpoint(request: MatchRoomRequest, current_user: User = Depends(get_current_user)):
    result = game.join_match_room(current_user.username, request.room_id)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/match/leave")
def leave_match_endpoint(current_user: User = Depends(get_current_user)):
    result = game.leave_match(current_user.username)
    return result

@app.get("/game/{game_id}/state")
def get_state(game_id: str, current_user: User = Depends(get_current_user)):
    state = game.get_game_state(game_id, current_user.username)
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    return state

@app.post("/game/{game_id}/move")
def submit_move(game_id: str, move: Move, current_user: User = Depends(get_current_user)):
    new_state = game.process_move(game_id, current_user.username, move)
    return new_state

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

@app.get("/cards")
def get_cards():
    return get_all_cards()

@app.get("/matchmaking/status")
def matchmaking_status(current_user: User = Depends(get_current_user)):
    status = game.get_matchmaking_status(current_user.username)
    return status