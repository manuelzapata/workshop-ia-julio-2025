from fastapi import APIRouter, HTTPException
from app.services.company_service import get_company_details

router = APIRouter(prefix='/company', tags=['Company'])

@router.get('/{company_id}', summary='Obtener detalles de una empresa', description='Devuelve los detalles de una empresa específica por ID')
def company_details(company_id: int) -> dict:
    details = get_company_details(company_id)
    if not details:
        raise HTTPException(status_code=404, detail='Empresa no encontrada')
    return details 