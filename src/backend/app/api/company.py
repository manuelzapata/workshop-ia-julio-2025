from fastapi import APIRouter, HTTPException, Depends
from app.services.company_service import CompanyService
from app.persistence.repositories.company_repository import CompanyRepository

router = APIRouter(prefix='/company', tags=['Company'])

def get_company_service():
    return CompanyService(CompanyRepository())

@router.get('/', summary='Listar empresas', description='Devuelve la lista de empresas con información básica')
async def list_companies(service: CompanyService = Depends(get_company_service)) -> list:
    return await service.get_companies_list()

@router.get('/{company_id}', summary='Obtener detalles de una empresa', description='Devuelve los detalles de una empresa específica por ID')
async def company_details(company_id: int, service: CompanyService = Depends(get_company_service)) -> dict:
    details = await service.get_company_details(company_id)
    if not details:
        raise HTTPException(status_code=404, detail='Empresa no encontrada')
    return details 