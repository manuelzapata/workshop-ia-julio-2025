from app.persistence.supabase_client import supabase_client

class CompanyRepository:
    async def get_company_by_id(self, company_id: int) -> dict | None:
        result = await supabase_client.get('/rest/v1/company', params={'id': f'eq.{company_id}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def get_by_name(self, name: str) -> dict | None:
        result = await supabase_client.get('/rest/v1/company', params={'name': f'eq.{name}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None
    
    async def get_all_companies_with_details(self, limit: int | None = None, offset: int = 0) -> list[dict]:
        # Get companies with optional pagination
        params = {}
        if limit is not None:
            params['limit'] = limit
            params['offset'] = offset
        
        companies = await supabase_client.get('/rest/v1/company', params=params)
        
        # Get all locations and industries (these are typically small datasets)
        locations = await supabase_client.get('/rest/v1/location')
        industries = await supabase_client.get('/rest/v1/industry')
        
        # Create lookup dictionaries
        location_lookup = {loc['id']: loc for loc in locations} if locations else {}
        industry_lookup = {ind['id']: ind for ind in industries} if industries else {}
        
        # Attach location and industry details to each company
        for company in companies:
            if company.get('location_id'):
                company['location'] = location_lookup.get(company['location_id'], {})
            if company.get('industry_id'):
                company['industry'] = industry_lookup.get(company['industry_id'], {})
        
        return companies 