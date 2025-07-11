import io
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Caso esperado: subir archivo válido
def test_upload_dataset_success():
    file_content = b'nombre,valor\nfoo,1\nbar,2'
    response = client.post(
        '/api/v1/dataset/upload',
        files={'file': ('test.csv', io.BytesIO(file_content), 'text/csv')}
    )
    assert response.status_code == 201
    assert response.json()['detail'] == 'Archivo procesado'
    assert response.json()['result']['filename'] == 'test.csv'

# Edge: subir archivo vacío
def test_upload_dataset_empty_file():
    response = client.post(
        '/api/v1/dataset/upload',
        files={'file': ('empty.csv', io.BytesIO(b''), 'text/csv')}
    )
    assert response.status_code == 201
    assert response.json()['result']['filename'] == 'empty.csv' 