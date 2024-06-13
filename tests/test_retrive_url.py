from fastapi.testclient import TestClient
from app import app
from routes.v1.shorten_url import url_repository, URLMapping

client = TestClient(app)

def setup_module(module):
    url_repository.clear()
    url_repository.update({
        "abc123": URLMapping(original_url="https://example.com/1", access_count=0),
    })

def test_get_original_url():
    response = client.get('/api/v1/retrive_url/abc123')
    print(response.json())
    assert response.status_code == 200

    # Teste para obter um alias que não existe
    response = client.get('/api/v1/retrive_url/invalid_alias')
    assert response.status_code == 404




