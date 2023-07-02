from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017/")
db = client["nombre_base_de_datos"]


@app.post("/register")
async def register_user(username: str, password: str):
    user = {
        "username": username,
        "password": password
    }
    collection = db["users"]
    result = await collection.insert_one(user)
    return {"message": "User registered successfully", "user_id": str(result.inserted_id)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
