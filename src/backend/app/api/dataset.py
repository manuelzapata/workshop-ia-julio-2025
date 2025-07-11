from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from app.services.dataset_service import DatasetService
from app.persistence.repositories.dataset_repository import DatasetRepository

router = APIRouter(prefix='/dataset', tags=['Dataset'])

def get_dataset_service():
    return DatasetService(DatasetRepository())

@router.post('/upload', status_code=status.HTTP_201_CREATED, summary='Carga manual del dataset', description='Permite cargar manualmente el dataset de empresas SaaS (protegido)')
async def upload_dataset(file: UploadFile = File(...), service: DatasetService = Depends(get_dataset_service)) -> dict:
    result = await service.process_dataset_upload(file)
    return {'detail': 'Archivo procesado', 'result': result} 