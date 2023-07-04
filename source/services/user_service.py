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

    async def create_user(self, user_data):
        return await self.database.create_user(user_data)

    async def get_user(self, user_id):
        return await self.database.get_user(user_id)

    async def update_user(self, user_id, user_data):
        return await self.database.update_user(user_id, user_data)
