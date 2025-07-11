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
def test_upload_dataset_success():
    class DummyRepo:
        async def bulk_insert(self, table, rows):
            return {'filename': 'test.csv'}
        def parse_csv(self, content):
            return [{'nombre': 'foo', 'valor': 1}, {'nombre': 'bar', 'valor': 2}]
    app.dependency_overrides[get_dataset_service] = lambda: DatasetService(DummyRepo())
    file_content = b'nombre,valor\nfoo,1\nbar,2'
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