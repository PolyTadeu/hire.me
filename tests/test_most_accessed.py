from fastapi.testclient import TestClient
from app import app
from routes.v1.shorten_url import url_repository, URLMapping

client = TestClient(app)

def setup_module(module):
    url_repository.clear()
    url_repository.update({
        "abc123": URLMapping(original_url="https://example.com/1", access_count=100),
        "def456": URLMapping(original_url="https://example.com/2", access_count=200),
    })

def test_get_most_accessed_urls():
    response = client.get("/api/v1/most_accessed")
    assert response.status_code == 200
    
    result = response.json()
    assert len(result) == 2

    # Verificar se o primeiro elemento é o esperado
    assert result[0]["original_url"] == "https://example.com/2" 
    assert result[1]["original_url"] == "https://example.com/1"
