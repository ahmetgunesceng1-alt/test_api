import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_endpoint():
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json() == {'message': 'hello world'}
    with open('test-results.txt', 'w') as f:
        f.write('Test passed: no issues found.')
