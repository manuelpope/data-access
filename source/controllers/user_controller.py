# controllers/user_controller.py
from fastapi import APIRouter, Depends, HTTPException
from services.user_service import UserService


class UserController:
    def __init__(self):
        self.router = APIRouter()
        self.user_service = UserService()

        self.router.post("/users")(self.create_user)
        self.router.get("/users/{user_id}")(self.get_user)
        self.router.put("/users/{user_id}")(self.update_user)

    async def create_user(self, user_data: dict, user_service: UserService = Depends()):
        user = await user_service.create_user(user_data)
        if user:
            return {"message": "User created successfully", "user": user}

        raise HTTPException(status_code=400, detail="User already exists")

    async def get_user(self, user_id: str, user_service: UserService = Depends()):
        user = await user_service.get_user(user_id)
        if user:
            return {"user": user}

        raise HTTPException(status_code=404, detail="User not found")

    async def update_user(self, user_id: str, user_data: dict, user_service: UserService = Depends()):
        try:
            user = await user_service.update_user(user_id, user_data)
            if user:
                return {"message": "User updated successfully", "user": user}
            else:
                raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
