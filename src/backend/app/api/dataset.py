from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from app.services.dataset_service import DatasetService
from app.persistence.repositories.dataset_repository import DatasetRepository

router = APIRouter(prefix='/dataset', tags=['Dataset'])

# Dependencia de protección (placeholder, se puede mejorar luego)
def get_admin_user():
    # Aquí se podría validar autenticación real
    return True

def get_dataset_service():
    return DatasetService(DatasetRepository())

@router.post('/upload', status_code=status.HTTP_201_CREATED, summary='Carga manual del dataset', description='Permite cargar manualmente el dataset de empresas SaaS (protegido)')
async def upload_dataset(file: UploadFile = File(...), admin: bool = Depends(get_admin_user), service: DatasetService = Depends(get_dataset_service)) -> dict:
    if not admin:
        raise HTTPException(status_code=401, detail='No autorizado')
    result = await service.process_dataset_upload(file)
    return {'detail': 'Archivo procesado', 'result': result} 