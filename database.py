from pymongo import MongoClient

MONGO_URI = "mongodb+srv://decofma:yznml9Yfd0P5CeN2@clusterzero.cgtsf.mongodb.net/"  # Ajuste conforme necessário
client = MongoClient(MONGO_URI)
db = client["pantheon_db"]
users_collection = db["users"]
games_collection = db["games"]
