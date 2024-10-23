class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, name, player_names):
        for player_name in player_names:
            query = """
            MATCH (p:Player {name: $player_name}) 
            CREATE (:Match {name: $name})<-[:PARTICIPA]-(p)
            """
            parameters = {"name": name, "player_name": player_name}
            self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_matches(self):
        query = """
        MATCH (m:Match)<-[:PARTICIPA]-(p:Player) 
        RETURN m.name AS match_name, p.name AS player_name
        """
        results = self.db.execute_query(query)
        matches = {}
        for result in results:
            match_name = result["match_name"]
            player_name = result["player_name"]
            if match_name not in matches:
                matches[match_name] = []
            matches[match_name].append(player_name)
        return matches

    def update_player(self, old_name, new_name):
        query = "MATCH (p:Player {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, player_name, match_name):
        query = """
        MATCH (p:Player {name: $player_name}), (m:Match {name: $match_name}) 
        CREATE (p)-[:PARTICIPA]->(m)
        """
        parameters = {"player_name": player_name, "match_name": match_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, name):
        query = "MATCH (m:Match {name: $name}) DETACH DELETE m"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
