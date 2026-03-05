import pytest
from fastapi.testclient import TestClient
from main import app

def test_hello_endpoint():
    client = TestClient(app)
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'hello world'}