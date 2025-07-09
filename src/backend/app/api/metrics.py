from fastapi import APIRouter
from app.services.metrics_service import get_general_metrics

router = APIRouter(prefix='/metrics', tags=['Metrics'])

@router.get('/', summary='Obtener métricas generales', description='Devuelve las métricas generales del dashboard')
def general_metrics() -> dict:
    return get_general_metrics() 