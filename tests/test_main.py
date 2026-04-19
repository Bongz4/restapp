from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/")
    assert response.status_code == 200

def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200

def test_create_user():
    response = client.post("/users", json={
        "id": 3,
        "name": "Test",
        "email": "test@test.com",
        "address": "SA",
        "mobile": "1111111111"
    })
    assert response.status_code == 200