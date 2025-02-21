# backend/game.py
import uuid
from models import GameState, Move
from typing import Dict, Any, List, Optional

# Filas e jogos ativos (em memória)
matchmaking_queue: List[str] = []
active_games: Dict[str, Dict[str, Any]] = {}

# Estrutura para salas (lobby) de partida
match_rooms: Dict[str, Dict[str, Any]] = {}

def initialize_deck(username: str):
    deck = list(range(1, 41))  # Exemplo: 40 cartas numeradas
    import random
    random.shuffle(deck)
    return deck

def draw_card(state: Dict[str, Any], player: str):
    if state["deck"][player]:
        card = state["deck"][player].pop(0)
        state["hand"][player].append(card)
        state["log"].append(f"{player} drew a card.")
    else:
        state["log"].append(f"{player} has no more cards to draw.")

def create_game_state(players: List[str]) -> Dict[str, Any]:
    game_id = str(uuid.uuid4())
    state = {
        "game_id": game_id,
        "players": players,
        "turn": players[0],
        "life_points": {players[0]: 50, players[1]: 50},
        "faith_points": {players[0]: 4, players[1]: 4},
        "hand": {players[0]: [], players[1]: []},
        "deck": {
            players[0]: initialize_deck(players[0]),
            players[1]: initialize_deck(players[1])
        },
        "field": {players[0]: [], players[1]: []},
        "log": [f"Game started between {players[0]} and {players[1]}."]
    }
    for player in players:
        for _ in range(7):
            draw_card(state, player)
    return state

def find_active_game(username: str) -> Optional[Dict[str, Any]]:
    for state in active_games.values():
        if username in state["players"]:
            return state
    return None

def join_matchmaking(username: str) -> Dict[str, Any]:
    # Se já estiver em uma partida ativa, retorne-a.
    existing = find_active_game(username)
    if existing:
        return existing
    # Se não estiver, adicione à fila.
    if username not in matchmaking_queue:
        matchmaking_queue.append(username)
    # Se houver pelo menos 2 na fila, crie a partida.
    if len(matchmaking_queue) >= 2:
        player1 = matchmaking_queue.pop(0)
        player2 = matchmaking_queue.pop(0)
        state = create_game_state([player1, player2])
        active_games[state["game_id"]] = state
        return state
    else:
        return {"message": "Waiting for an opponent."}

def create_match_room(username: str, room_id: str) -> Dict[str, Any]:
    if room_id in match_rooms:
        return {"error": "Sala já existe"}
    room = {
        "room_id": room_id,
        "players": [username],
        "status": "waiting",
        "game_state": None,
    }
    match_rooms[room_id] = room
    return room

def join_match_room(username: str, room_id: str) -> Dict[str, Any]:
    if room_id not in match_rooms:
        return {"error": "Sala não encontrada"}
    room = match_rooms[room_id]
    if username in room["players"]:
        return room
    if len(room["players"]) >= 2:
        return {"error": "Sala já está completa"}
    room["players"].append(username)
    if len(room["players"]) == 2:
        room["status"] = "started"
        room["game_state"] = create_game_state(room["players"])
        active_games[room["game_state"]["game_id"]] = room["game_state"]
    return room

def leave_match(username: str) -> Dict[str, Any]:
    # Remove de fila de matchmaking, se presente.
    if username in matchmaking_queue:
        matchmaking_queue.remove(username)
    # Procura se o usuário está em alguma sala.
    for room_id, room in list(match_rooms.items()):
        if username in room["players"]:
            room["players"].remove(username)
            # Se a sala ficar vazia, remove-a.
            if not room["players"]:
                del match_rooms[room_id]
            else:
                room["status"] = "waiting"
            return {"message": "Você abandonou a sala."}
    # Procura se o usuário está em um jogo ativo.
    for game_id, state in list(active_games.items()):
        if username in state["players"]:
            del active_games[game_id]
            return {"message": "Partida abandonada."}
    return {"message": "Nenhuma partida ativa encontrada."}

def get_game_state(game_id: str, username: str):
    state = active_games.get(game_id)
    if state and username in state["players"]:
        return state
    return None

def process_move(game_id: str, username: str, move: Move):
    state = active_games.get(game_id)
    if not state:
        return {"error": "Game not found."}
    if state["turn"] != username:
        return {"error": "Not your turn."}
    
    if move.move_type == "invocar":
        card_id = move.data.get("card_id")
        if card_id in state["hand"][username]:
            state["hand"][username].remove(card_id)
            state["field"][username].append(card_id)
            state["log"].append(f"{username} summoned card {card_id}.")
            cost = move.data.get("cost", 3)
            state["faith_points"][username] -= cost
        else:
            state["log"].append(f"{username} does not have card {card_id} in hand.")
    elif move.move_type == "atacar":
        damage = move.data.get("damage", 3)
        opponent = [p for p in state["players"] if p != username][0]
        state["life_points"][opponent] -= damage
        state["log"].append(f"{username} attacked {opponent} for {damage} damage.")
    elif move.move_type == "evento":
        state["log"].append(f"{username} played an event card.")
    else:
        state["log"].append(f"{username} performed an unknown move.")
    
    # Fim do turno: regenerar pontos de fé e comprar carta para ambos.
    state["faith_points"][username] += 4
    draw_card(state, username)
    opponent = [p for p in state["players"] if p != username][0]
    state["turn"] = opponent
    state["faith_points"][opponent] += 4
    draw_card(state, opponent)
    
    return state
