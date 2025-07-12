import io
import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
from app.api.dataset import get_dataset_service, DatasetService

os.environ['supabase_url'] = 'http://test-url'
os.environ['supabase_key'] = 'test-key'
os.environ['environment'] = 'test'

client = TestClient(app)

# Caso esperado: subir archivo válido
def test_upload_dataset_success(monkeypatch):
    # Mock principal repo
    class DummyRepo:
        async def bulk_insert(self, table, rows):
            return {'filename': 'test.csv'}
        def parse_csv(self, content):
            return [{'name': 'foo', 'value': 1}, {'name': 'bar', 'value': 2}]
    # Mock secundarios
    class DummyIndustryRepo:
        async def bulk_insert(self, items): return None
        async def get_by_name(self, name): return {'id': 1}
    class DummyLocationRepo:
        async def bulk_insert(self, items): return None
        async def get_by_fields(self, city, state_province, country): return {'id': 1}
    class DummyInvestorRepo:
        async def bulk_insert(self, items): return None
    # Mock supabase_client.get para company
    async def fake_get(path, params=None):
        if path == '/rest/v1/company':
            return [{'id': 1, 'name': params['name'].split('.')[-1]}]
        return []
    monkeypatch.setattr('app.services.dataset_service.IndustryRepository', lambda: DummyIndustryRepo())
    monkeypatch.setattr('app.services.dataset_service.LocationRepository', lambda: DummyLocationRepo())
    monkeypatch.setattr('app.services.dataset_service.InvestorRepository', lambda: DummyInvestorRepo())
    monkeypatch.setattr('app.persistence.supabase_client.supabase_client.get', fake_get)
    app.dependency_overrides[get_dataset_service] = lambda: DatasetService(DummyRepo())
    file_content = b'name,value\nfoo,1\nbar,2'
    response = client.post(
        '/api/v1/dataset/upload',
        files={'file': ('test.csv', io.BytesIO(file_content), 'text/csv')}
    )
    assert response.status_code == 201
    assert response.json()['detail'] == 'Archivo procesado'
    assert response.json()['result']['inserted'] == 2
    assert response.json()['result']['result']['filename'] == 'test.csv'
    app.dependency_overrides = {}

# Edge: subir archivo vacío
def test_upload_dataset_empty_file():
    class DummyRepo:
        async def bulk_insert(self, table, rows):
            return {'filename': 'empty.csv'}
        def parse_csv(self, content):
            return []
    app.dependency_overrides[get_dataset_service] = lambda: DatasetService(DummyRepo())
    response = client.post(
        '/api/v1/dataset/upload',
        files={'file': ('empty.csv', io.BytesIO(b''), 'text/csv')}
    )
    assert response.status_code == 201
    assert response.json()['result']['inserted'] == 0
    assert response.json()['result']['result']['filename'] == 'empty.csv'
    app.dependency_overrides = {} 