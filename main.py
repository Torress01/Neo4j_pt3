from database import Database
from game_database import GameDatabase

db = Database("neo4j+s://7105a606.databases.neo4j.io", "neo4j", "g13SA4kWcQLlsfcgIq3Cc2QiLgBvybZk1oiq_LwZ6Bc")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("leozin")
game_db.create_player("Aninha")
game_db.create_player("Zézin")

game_db.create_match("Partida de Tenis", ["leozin", "Aninha"])
game_db.create_match("Partida de Futebol", ["Aninha", "Zézin"])
game_db.create_match("Partida de Truco", ["Zézin", "leozin"])


game_db.update_player("leozin", "Pedrin")

game_db.insert_player_match("Ana", "Partida de Tenis")
game_db.insert_player_match("Pedrin", "Partida de Truco")

print("Jogadores:")
print(game_db.get_players())
print("Partidas e jogadores participantes:")
print(game_db.get_matches())

game_db.delete_player("Carlos")
game_db.delete_match("Partida de Truco")

db.close()
