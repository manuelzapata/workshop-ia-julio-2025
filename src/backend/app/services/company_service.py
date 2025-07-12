from app.persistence.repositories.company_repository import CompanyRepository
from app.utils.location_formatter import format_location

class CompanyService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    async def get_company_details(self, company_id: int) -> dict | None:
        return await self.repository.get_company_by_id(company_id)
    
    async def get_companies_list(self) -> list:
        companies = await self.repository.get_all_companies_with_details()
        
        # Format the response
        formatted_companies = []
        for company in companies:
            # Get location details
            location = company.get('location', {})
            location_str = format_location(location)
            
            # Get industry details
            industry = company.get('industry', {})
            
            formatted_company = {
                'id': company.get('id'),
                'name': company.get('name'),
                'founded_year': company.get('founded_year'),
                'revenue': company.get('arr'),  # ARR as revenue
                'valuation': company.get('valuation'),
                'sector': industry.get('name', 'Unknown'),
                'location': location_str
            }
            formatted_companies.append(formatted_company)
        
        # Sort by revenue descending
        formatted_companies.sort(key=lambda x: x.get('revenue', 0) or 0, reverse=True)
        
        return formatted_companies
 