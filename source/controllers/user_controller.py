# controllers/user_controller.py
from fastapi import APIRouter
from services.user_service import UserService


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.user_service = UserService()

        self.router.post("/users")(self.create_user)
        self.router.get("/users/{user_id}")(self.get_user)
        self.router.put("/users/{user_id}")(self.update_user)

    def create_user(self, user_data: dict):
        user = self.user_service.create_user(user_data)
        return {"message": "User created successfully", "user": user}

    def get_user(self, user_id: str):
        user = self.user_service.get_user(user_id)
        return {"user": user}

    def update_user(self, user_id: str, user_data: dict):
        user = self.user_service.update_user(user_id, user_data)
        return {"message": "User updated successfully", "user": user}
