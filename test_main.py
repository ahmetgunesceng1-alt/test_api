import pytest
import json
from main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_endpoint(client):
    response = client.get('/hello')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {'message': 'hello world'}