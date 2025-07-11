from app.persistence.supabase_client import supabase_client

class CompanyInvestorRepository:
    async def get_by_ids(self, company_id: int, investor_id: int) -> dict | None:
        params = {'company_id': f'eq.{company_id}', 'investor_id': f'eq.{investor_id}'}
        result = await supabase_client.get('/rest/v1/company_investor', params=params)
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, relations: list[dict]) -> list[dict]:
        inserted = []
        for rel in relations:
            company_id = rel['company_id']
            investor_id = rel['investor_id']
            existing = await self.get_by_ids(company_id, investor_id)
            if not existing:
                data = {'company_id': company_id, 'investor_id': investor_id}
                res = await supabase_client.post('/rest/v1/company_investor', [data])
                inserted.append(res)
        return inserted 