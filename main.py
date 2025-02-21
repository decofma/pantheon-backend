from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta
import uvicorn
from models import User, Move
import auth
import game
import os


# Configurações do JWT
SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou use ["*"] para permitir todos (em desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de registro
@app.post("/auth/register")
def register(user: auth.UserCreate):
    return auth.register_user(user, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

# Endpoint de login
@app.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.authenticate_user(form_data.username, form_data.password, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES)

def get_current_user(token: str = Depends(auth.oauth2_scheme)):
    return auth.get_current_user(token, SECRET_KEY, ALGORITHM)

# Endpoint para entrar no matchmaking
@app.post("/matchmaking/join")
def join_matchmaking(current_user: User = Depends(get_current_user)):
    game_state = game.join_matchmaking(current_user.username)
    return game_state

# Endpoint para obter o estado do jogo
@app.get("/game/{game_id}/state")
def get_state(game_id: str, current_user: User = Depends(get_current_user)):
    state = game.get_game_state(game_id, current_user.username)
    if not state:
        raise HTTPException(status_code=404, detail="Game not found")
    return state

# Endpoint para enviar uma jogada
@app.post("/game/{game_id}/move")
def submit_move(game_id: str, move: Move, current_user: User = Depends(get_current_user)):
    new_state = game.process_move(game_id, current_user.username, move)
    return new_state

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
