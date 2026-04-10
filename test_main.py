from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_soma():
    response = client.get("/somar/2/2")
    assert response.json() == {"resultado": 4}
