# backend/game.py
import uuid
from models import GameState, Move
from typing import Dict, Any, List, Optional

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
    # Cada jogador inicia com 7 cartas e 4 pontos de fé (na fase de preparação)
    for player in players:
        for _ in range(7):
            draw_card(state, player)
        state["faith_points"][player] = 4
    return state

def find_active_game(username: str) -> Optional[Dict[str, Any]]:
    for state in active_games.values():
        if username in state["players"]:
            return state
    return None

def join_matchmaking(username: str) -> Dict[str, Any]:
    existing = find_active_game(username)
    if existing:
        return existing
    if username not in matchmaking_queue:
        matchmaking_queue.append(username)
    if len(matchmaking_queue) >= 2:
        player1 = matchmaking_queue.pop(0)
        player2 = matchmaking_queue.pop(0)
        state = create_game_state([player1, player2])
        active_games[state["game_id"]] = state
        return state
    else:
        return {"message": "Waiting for an opponent."}

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
    """
    process_move espera que move.data contenha uma chave 'phase' para indicar a fase em que o movimento se aplica.
    
    Fases:
      - "preparation": O jogador recebe 4 pontos de fé e compra 1 carta.
      - "invocation": O jogador joga uma carta (deus, artefato ou criatura) pagando seu custo em pontos de fé.
      - "combat": O jogador declara ataques. O dano (possivelmente modificado por atributos) é aplicado ao adversário.
      - "event": O jogador joga uma carta de evento que pode, por exemplo, causar dano direto ou curar.
      
    Ao final da fase de evento, o turno é encerrado e a vez passa para o adversário, reiniciando a fase de preparação.
    """
    state = active_games.get(game_id)
    if not state:
        return {"error": "Game not found."}
    if state["turn"] != username:
        return {"error": "Not your turn."}
    
    # O movimento deve indicar em qual fase ele ocorre
    const_phase = move.data.get("phase")
    if not const_phase:
        return {"error": "Phase not specified in move."}
    
    current_phase = state.get("phase", "preparation")
    if const_phase != current_phase:
        return {"error": f"Invalid move for current phase: {current_phase}."}
    
    if current_phase == "preparation":
        # Preparação: adquire 4 pontos de fé e compra 1 carta.
        state["faith_points"][username] += 4
        draw_card(state, username)
        state["log"].append(f"{username} completed preparation phase.")
        # Passa para a fase de invocação.
        state["phase"] = "invocation"
    
    elif current_phase == "invocation":
        # Invocação: jogar uma carta, pagando o custo.
        card_id = move.data.get("card_id")
        cost = move.data.get("cost", 0)
        if state["faith_points"][username] < cost:
            return {"error": "Not enough faith points."}
        if card_id in state["hand"][username]:
            state["hand"][username].remove(card_id)
            state["field"][username].append(card_id)
            state["faith_points"][username] -= cost
            state["log"].append(f"{username} played card {card_id} in invocation phase.")
        else:
            return {"error": "Card not found in hand."}
        # Para simplificar, uma ação de invocação encerra a fase.
        state["phase"] = "combat"
    
    elif current_phase == "combat":
        # Combate: declarar ataque.
        # Espera-se que move.data contenha "damage".
        damage = move.data.get("damage", 0)
        # Aqui, você poderia aplicar os modificadores de atributos conforme a tabela.
        opponent = [p for p in state["players"] if p != username][0]
        state["life_points"][opponent] -= damage
        state["log"].append(f"{username} attacked {opponent} for {damage} damage in combat phase.")
        # Avança para a fase de evento.
        state["phase"] = "event"
    
    elif current_phase == "event":
        # Evento: jogar carta de evento.
        event_card = move.data.get("card_id")
        cost = move.data.get("cost", 0)
        if state["faith_points"][username] < cost:
            return {"error": "Not enough faith points for event."}
        if event_card in state["hand"][username]:
            state["hand"][username].remove(event_card)
            state["faith_points"][username] -= cost
            state["log"].append(f"{username} played event card {event_card} in event phase.")
            # Exemplo: efeito do evento - dano direto.
            event_damage = move.data.get("effect_damage", 0)
            opponent = [p for p in state["players"] if p != username][0]
            state["life_points"][opponent] -= event_damage
        else:
            return {"error": "Event card not found in hand."}
        # Fim do turno: reinicia a fase para preparação e troca o turno.
        state["phase"] = "preparation"
        opponent = [p for p in state["players"] if p != username][0]
        state["turn"] = opponent
        # O novo turno começará com a preparação do adversário.
    
    else:
        return {"error": "Unknown phase."}
    
    return state
