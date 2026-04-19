from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Load data
def load_users():
    with open("app/user.json") as f:
        return json.load(f)["users"]

def save_users(users):
    with open("app/user.json", "w") as f:
        json.dump({"users": users}, f, indent=4)

# GET all users
@app.get("/")
def get_all_users():
    return load_users()

# GET user by ID
@app.get("/user/{uid}")
def get_user(uid: int):
    users = load_users()
    for user in users:
        if user["id"] == uid:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# POST - create user
@app.post("/users")
def create_user(user: dict):
    users = load_users()
    users.append(user)
    save_users(users)
    return {"message": "User added"}

# PUT - update user
@app.put("/users/{uid}")
def update_user(uid: int, updated_user: dict):
    users = load_users()
    for i, user in enumerate(users):
        if user["id"] == uid:
            users[i] = updated_user
            save_users(users)
            return {"message": "User updated"}
    raise HTTPException(status_code=404, detail="User not found")

# DELETE user
@app.delete("/users/{uid}")
def delete_user(uid: int):
    users = load_users()
    for user in users:
        if user["id"] == uid:
            users.remove(user)
            save_users(users)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")