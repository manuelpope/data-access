# services/database.py
from pymongo import MongoClient


class MongoDBDatabase:
    def __init__(self, mongo_uri):
        self.client = MongoClient(mongo_uri)
        self.db = self.client["mydatabase"]
        self.users_collection = self.db["users"]

    def create_user(self, user_data):
        # Lógica para crear un usuario en la base de datos MongoDB
        pass

    def get_user(self, user_id):
        # Lógica para obtener un usuario de la base de datos MongoDB
        pass

    def update_user(self, user_id, user_data):
        # Lógica para actualizar un usuario en la base de datos MongoDB
        pass


# services/database.py
class InMemoryDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, user_data):
        user_id = user_data.get("id")
        if user_id not in self.users:
            self.users[user_id] = user_data
            return user_data
        return None

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, user_data):
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return self.users[user_id]
        return None
