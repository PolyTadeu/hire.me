from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_shorten_url():
    #URL válida e sem alias customizado
    response = client.post('/api/v1/shorten_url?url=https://example.com')
    assert response.status_code == 200
    data = response.json()
    assert 'alias' in data
    assert 'short_url' in data
    assert 'original_url' in data

    #URL válida e um alias customizado
    response = client.post('/api/v1/shorten_url/?url=https://example.com&custom_alias=example')
    assert response.status_code == 200
    data = response.json()
    assert data['alias'] == 'example'

    #Alias que já existe
    response = client.post('/api/v1/shorten_url?url=https://example.com&custom_alias=example')
    assert response.status_code == 400  # Deve retornar erro de alias já existente





