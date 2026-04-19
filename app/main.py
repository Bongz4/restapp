from fastapi import FastAPI, HTTPException
import json

app = FastAPI()


def load_users():
    with open("app/user.json") as f:
        return json.load(f)["users"]


def save_users(users):
    with open("app/user.json", "w") as f:
        json.dump({"users": users}, f, indent=4)


@app.get("/")
def home():
    return {"message": "CI/CD triggered - updated version"}


@app.get("/user/{uid}")
def get_user(uid: int):
    users = load_users()
    for user in users:
        if user["id"] == uid:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/users")
def create_user(user: dict):
    users = load_users()
    users.append(user)
    save_users(users)
    return {"message": "User added"}


@app.put("/users/{uid}")
def update_user(uid: int, updated_user: dict):
    users = load_users()
    for i, user in enumerate(users):
        if user["id"] == uid:
            users[i] = updated_user
            save_users(users)
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{uid}")
def delete_user(uid: int):
    users = load_users()
    for user in users:
        if user["id"] == uid:
            users.remove(user)
            save_users(users)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
