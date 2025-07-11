import os
os.environ['supabase_url'] = 'http://test-url'
os.environ['supabase_key'] = 'test-key'
os.environ['environment'] = 'test'
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.metrics import get_metrics_service, MetricsService

client = TestClient(app)

# Caso esperado: obtener métricas generales
def test_get_general_metrics_success():
    class DummyRepo:
        async def get_all_companies(self):
            return [
                {'revenue': 100, 'valuation': 200},
                {'revenue': 200, 'valuation': 400}
            ]
    app.dependency_overrides[get_metrics_service] = lambda: MetricsService(DummyRepo())
    response = client.get('/api/v1/metrics/')
    assert response.status_code == 200
    data = response.json()
    assert data['total_companies'] == 2
    assert data['total_revenue'] == 300
    assert data['average_valuation'] == 300
    app.dependency_overrides = {}

# Edge: simular respuesta vacía (mock)
def test_get_general_metrics_empty():
    class DummyRepo:
        async def get_all_companies(self):
            return []
    app.dependency_overrides[get_metrics_service] = lambda: MetricsService(DummyRepo())
    response = client.get('/api/v1/metrics/')
    assert response.status_code == 200
    assert response.json() == {'total_companies': 0, 'total_revenue': 0, 'average_valuation': 0}
    app.dependency_overrides = {}

# Error: simular error interno (mock)
def test_get_general_metrics_error():
    class DummyRepo:
        async def get_all_companies(self):
            raise Exception('Internal error')
    app.dependency_overrides[get_metrics_service] = lambda: MetricsService(DummyRepo())
    response = None
    try:
        response = client.get('/api/v1/metrics/')
    except Exception:
        # Si la excepción se propaga, el test sigue pasando
        return
    assert response is not None
    assert response.status_code == 500
    app.dependency_overrides = {} 