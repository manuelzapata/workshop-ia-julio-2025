from fastapi import APIRouter, Depends
from app.services.metrics_service import MetricsService
from app.persistence.repositories.metrics_repository import MetricsRepository

router = APIRouter(prefix='/metrics', tags=['Metrics'])

def get_metrics_service():
    return MetricsService(MetricsRepository())

@router.get('/', summary='Obtener métricas generales', description='Devuelve las métricas generales del dashboard')
async def general_metrics(service: MetricsService = Depends(get_metrics_service)) -> dict:
    return await service.get_general_metrics() 