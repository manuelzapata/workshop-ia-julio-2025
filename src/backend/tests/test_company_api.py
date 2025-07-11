import os
os.environ['supabase_url'] = 'http://test-url'
os.environ['supabase_key'] = 'test-key'
os.environ['environment'] = 'test'


import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.company import get_company_service, CompanyService

client = TestClient(app)

# Caso esperado: obtener detalles de empresa existente (ID=1)
def test_get_company_details_success():
    class DummyRepo:
        async def get_company_by_id(self, company_id):
            return {'id': 1, 'name': 'Acme SaaS'}
    app.dependency_overrides[get_company_service] = lambda: CompanyService(DummyRepo())
    response = client.get('/api/v1/company/1')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert data['name'] == 'Acme SaaS'
    app.dependency_overrides = {}

# Edge: empresa con ID=0 o negativo
def test_get_company_details_edge():
    class DummyRepo:
        async def get_company_by_id(self, company_id):
            return None
    app.dependency_overrides[get_company_service] = lambda: CompanyService(DummyRepo())
    response = client.get('/api/v1/company/0')
    assert response.status_code == 404
    response = client.get('/api/v1/company/-1')
    assert response.status_code == 404
    app.dependency_overrides = {}

# Error: empresa no encontrada (ID no existente)
def test_get_company_details_not_found():
    class DummyRepo:
        async def get_company_by_id(self, company_id):
            return None
    app.dependency_overrides[get_company_service] = lambda: CompanyService(DummyRepo())
    response = client.get('/api/v1/company/999')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Empresa no encontrada'
    app.dependency_overrides = {} 