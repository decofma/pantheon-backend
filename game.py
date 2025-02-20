import uuid
from models import GameState, Move
from typing import Dict, Any

# Filas e jogos ativos (em memória)
matchmaking_queue = []
active_games = {}

def join_matchmaking(username: str) -> Dict[str, Any]:
    if username not in matchmaking_queue:
        matchmaking_queue.append(username)
    
    if len(matchmaking_queue) >= 2:
        player1 = matchmaking_queue.pop(0)
        player2 = matchmaking_queue.pop(0)
        game_id = str(uuid.uuid4())
        state = {
            "game_id": game_id,
            "players": [player1, player2],
            "turn": player1,
            "life_points": {player1: 50, player2: 50},
            "faith_points": {player1: 4, player2: 4},
            "hand": {player1: [], player2: []},
            "deck": {player1: initialize_deck(player1), player2: initialize_deck(player2)},
            "field": {player1: [], player2: []},
            "log": [f"Game started between {player1} and {player2}."]
        }
        # Cada jogador compra 7 cartas iniciais
        for player in [player1, player2]:
            for _ in range(7):
                draw_card(state, player)
        active_games[game_id] = state
        return state
    else:
        return {"message": "Waiting for an opponent."}

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
    
    # Fim do turno: regenerar pontos de fé e comprar carta para ambos
    state["faith_points"][username] += 4
    draw_card(state, username)
    opponent = [p for p in state["players"] if p != username][0]
    state["turn"] = opponent
    state["faith_points"][opponent] += 4
    draw_card(state, opponent)
    
    return state
