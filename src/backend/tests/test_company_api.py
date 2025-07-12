import os
os.environ['supabase_url'] = 'http://test-url'
os.environ['supabase_key'] = 'test-key'
os.environ['environment'] = 'test'


import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api.company import get_company_service, CompanyService
import asyncio

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

def test_bulk_insert_investor(monkeypatch):
    from app.persistence.repositories.investor_repository import InvestorRepository
    calls = {}
    async def fake_get(path, params=None):
        calls['get'] = params
        # Simula que ya existe 'A', pero no 'B'
        if params and 'in.' in params.get('name', ''):
            return [{'name': 'A'}]
        return []
    async def fake_post(path, data=None):
        calls['post'] = data
        return {'name': data[0]['name']}
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.get', fake_get)
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.post', fake_post)
    repo = InvestorRepository()
    result = asyncio.run(repo.bulk_insert(['A', 'B']))
    assert result == [{'name': 'B'}]
    assert calls['get']['name'].startswith('in.')
    assert calls['post'][0]['name'] == 'B'

def test_bulk_insert_investor_empty(monkeypatch):
    from app.persistence.repositories.investor_repository import InvestorRepository
    repo = InvestorRepository()
    result = asyncio.run(repo.bulk_insert([]))
    assert result == []

def test_bulk_insert_industry(monkeypatch):
    from app.persistence.repositories.industry_repository import IndustryRepository
    async def fake_get(path, params=None):
        if params and 'in.' in params.get('name', ''):
            return [{'name': 'X'}]
        return []
    async def fake_post(path, data=None):
        return {'name': data[0]['name']}
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.get', fake_get)
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.post', fake_post)
    repo = IndustryRepository()
    result = asyncio.run(repo.bulk_insert(['X', 'Y']))
    assert result == [{'name': 'Y'}]

def test_bulk_insert_location(monkeypatch):
    from app.persistence.repositories.location_repository import LocationRepository
    async def fake_get(path, params=None):
        # Simula que ya existe una ubicación
        return [{'city': 'C', 'state_province': 'S', 'country': 'P'}]
    async def fake_post(path, data=None):
        return data[0]
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.get', fake_get)
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.post', fake_post)
    repo = LocationRepository()
    result = asyncio.run(repo.bulk_insert([
        {'city': 'C', 'state_province': 'S', 'country': 'P'},
        {'city': 'N', 'state_province': 'S', 'country': 'P'}
    ]))
    assert result == [{'city': 'N', 'state_province': 'S', 'country': 'P'}]

def test_bulk_insert_company_investor(monkeypatch):
    from app.persistence.repositories.company_investor_repository import CompanyInvestorRepository
    async def fake_get(path, params=None):
        # Simula que ya existe una relación
        return [{'company_id': 1, 'investor_id': 2}]
    async def fake_post(path, data=None):
        return data[0]
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.get', fake_get)
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.post', fake_post)
    repo = CompanyInvestorRepository()
    result = asyncio.run(repo.bulk_insert([
        {'company_id': 1, 'investor_id': 2},
        {'company_id': 2, 'investor_id': 3}
    ]))
    assert result == [{'company_id': 2, 'investor_id': 3}] 