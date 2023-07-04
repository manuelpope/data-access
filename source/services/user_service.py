# services/user_service.py
import os
from database.database import InMemoryDatabase, MongoDBDatabase


class UserService:
    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI")
        if mongo_uri:
            self.database = MongoDBDatabase(mongo_uri)
        else:
            self.database = InMemoryDatabase()

    def create_user(self, user_data):
        return self.database.create_user(user_data)

    def get_user(self, user_id):
        return self.database.get_user(user_id)

    def update_user(self, user_id, user_data):
        return self.database.update_user(user_id, user_data)
