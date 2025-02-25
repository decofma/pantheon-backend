# backend/game.py
import uuid
from models import GameState, Move
from typing import Dict, Any, List, Optional
from cards import get_card_by_id
from database import games_collection

# Variáveis globais
matchmaking_queue: List[str] = []
active_games: Dict[str, Dict[str, Any]] = {}
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
        "faith_points": {players[0]: 0, players[1]: 0},
        "hand": {players[0]: [], players[1]: []},
        "deck": {
            players[0]: initialize_deck(players[0]),
            players[1]: initialize_deck(players[1])
        },
        "field": {players[0]: [], players[1]: []},
        "log": [f"Game started between {players[0]} and {players[1]}."],
        "phase": "preparation"  # Inicia no turno de preparação
    }
    games_collection.insert_one(state.copy())
    return state

def get_matchmaking_status(username: str) -> Dict[str, Any]:
    """
    Retorna o estado do jogo se o jogador já tiver sido emparelhado;
    caso contrário, retorna uma mensagem informando que está aguardando um oponente.
    """
    game_state = find_active_game(username)
    if game_state:
        return game_state
    return {"message": "Waiting for an opponent."}

def find_active_game(username: str) -> Optional[Dict[str, Any]]:
    for state in active_games.values():
        if username in state["players"]:
            return state
    return None

def join_matchmaking(username: str) -> Dict[str, Any]:
    existing = find_active_game(username)
    if existing:
        return existing
    
    # Adiciona à fila se não estiver cheio
    if username not in matchmaking_queue:
        matchmaking_queue.append(username)
    
    # Tenta emparelhar jogadores a cada chamada
    while len(matchmaking_queue) >= 2:
        player1 = matchmaking_queue.pop(0)
        player2 = matchmaking_queue.pop(0)
        state = create_game_state([player1, player2])
        active_games[state["game_id"]] = state
        return state
    
    return {"message": "Aguardando oponente..."}

# Funções para salas customizadas (não modificadas aqui)
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

def get_game_state(game_id: str, username: str):
    state = games_collection.find_one(
        {"game_id": game_id, "players": username}
    )
    return state

# Modifique a função join_match_room para retornar o estado correto
def join_match_room(username: str, room_id: str) -> Dict[str, Any]:
    if room_id not in match_rooms:
        return {"error": "Sala não encontrada"}
    
    room = match_rooms[room_id]
    
    if username in room["players"]:
        return {
            "status": room["status"],
            "game_state": room.get("game_state"),
            "room_id": room_id,
            "players": room["players"]
        }
    
    if len(room["players"]) >= 2:
        return {"error": "Sala já está completa"}
    
    room["players"].append(username)
    
    if len(room["players"]) == 2:
        room["status"] = "started"
        game_state = create_game_state(room["players"])
        room["game_state"] = game_state
        active_games[game_state["game_id"]] = game_state
        
    return {
        "status": room["status"],
        "game_state": room.get("game_state"),
        "room_id": room_id,
        "players": room["players"]
    }

def leave_match(username: str) -> Dict[str, Any]:
    if username in matchmaking_queue:
        matchmaking_queue.remove(username)
    for room_id, room in list(match_rooms.items()):
        if username in room["players"]:
            room["players"].remove(username)
            if not room["players"]:
                del match_rooms[room_id]
            else:
                room["status"] = "waiting"
            return {"message": "Você abandonou a sala."}
    for game_id, state in list(active_games.items()):
        if username in state["players"]:
            del active_games[game_id]
            return {"message": "Partida abandonada."}
    return {"message": "Nenhuma partida ativa encontrada."}

def process_move(game_id: str, username: str, move: Move) -> Dict[str, Any]:
    state = active_games.get(game_id)
    if not state:
        return {"error": "Game not found."}
    if state["turn"] != username:
        return {"error": "Not your turn."}
    
    # Espera que move.data contenha a fase e o id da carta selecionada
    phase = move.data.get("phase")
    selected_card = move.data.get("selected_card")
    
    if phase not in ["invocation", "combat", "event"]:
        return {"error": "Invalid phase for card play."}
    
    if phase == "invocation":
        if selected_card not in state["hand"][username]:
            return {"error": "Card not found in hand."}
        card_detail = get_card_by_id(selected_card)
        if not card_detail:
            return {"error": "Invalid card."}
        cost = card_detail.get("custo_fe", 0)
        if state["faith_points"][username] < cost:
            return {"error": "Not enough faith points."}
        state["hand"][username].remove(selected_card)
        state["field"][username].append(selected_card)
        state["faith_points"][username] -= cost
        state["log"].append(f"{username} invoked {card_detail['nome']}.")
        # Após invocação, o estado pode avançar para a fase de combate
        state["phase"] = "combat"
    
    # Para outras fases, implemente lógica semelhante (por exemplo, para 'combat' ou 'event')
    elif phase == "combat":
        # Neste exemplo, o movimento de combate poderia especificar um ataque com um card da field.
        damage = move.data.get("damage", 0)
        opponent = [p for p in state["players"] if p != username][0]
        state["life_points"][opponent] -= damage
        state["log"].append(f"{username} attacked {opponent} for {damage} damage in combat phase.")
        state["phase"] = "event"
    
    elif phase == "event":
        # Processamento de carta de evento, semelhante à invocação
        event_card = selected_card  # Supomos que o jogador selecionou uma carta de evento
        if event_card not in state["hand"][username]:
            return {"error": "Event card not found in hand."}
        card_detail = get_card_by_id(event_card)
        if not card_detail:
            return {"error": "Invalid event card."}
        cost = card_detail.get("custo_fe", 0)
        if state["faith_points"][username] < cost:
            return {"error": "Not enough faith points for event."}
        state["hand"][username].remove(event_card)
        state["faith_points"][username] -= cost
        state["log"].append(f"{username} played event card {card_detail['nome']} in event phase.")
        # Exemplo: se o evento causa dano direto
        event_damage = move.data.get("effect_damage", 0)
        opponent = [p for p in state["players"] if p != username][0]
        state["life_points"][opponent] -= event_damage
        # Encerra o turno, reiniciando para preparação e trocando o turno
        state["phase"] = "preparation"
        state["turn"] = opponent
        # Na preparação do novo turno, o adversário receberá os bônus de fé e comprará uma carta (processo separado)
    
    return state
