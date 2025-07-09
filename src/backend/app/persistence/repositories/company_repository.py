from app.persistence.supabase_client import supabase_client

class CompanyRepository:
    async def get_company_by_id(self, company_id: int) -> dict | None:
        result = await supabase_client.get('/rest/v1/company', params={'id': f'eq.{company_id}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None 