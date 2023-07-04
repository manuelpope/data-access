# main.py
from fastapi import FastAPI

from controllers.user_controller import UserController

app = FastAPI()

# Inicializar controlador de usuarios
user_controller = UserController()

# Rutas
app.include_router(user_controller.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
