import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Caso esperado: obtener detalles de empresa existente (ID=1)
def test_get_company_details_success():
    response = client.get('/api/v1/company/1')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert data['name'] == 'Acme SaaS'

# Edge: empresa con ID=0 o negativo
def test_get_company_details_edge():
    response = client.get('/api/v1/company/0')
    assert response.status_code == 404
    response = client.get('/api/v1/company/-1')
    assert response.status_code == 404

# Error: empresa no encontrada (ID no existente)
def test_get_company_details_not_found():
    response = client.get('/api/v1/company/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Empresa no encontrada' 