from fastapi import APIRouter
from src.backend.core.config import settings

router = APIRouter()

@router.get('/health', tags=['Health'])
def health_check() -> dict:
    return {'status': 'ok', 'environment': settings.environment} 