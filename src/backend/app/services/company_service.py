from app.persistence.repositories.company_repository import CompanyRepository

class CompanyService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    async def get_company_details(self, company_id: int) -> dict | None:
        return await self.repository.get_company_by_id(company_id) 