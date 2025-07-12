from app.persistence.supabase_client import supabase_client

class CompanyInvestorRepository:
    async def get_by_ids(self, company_id: int, investor_id: int) -> dict | None:
        params = {'company_id': f'eq.{company_id}', 'investor_id': f'eq.{investor_id}'}
        result = await supabase_client.get('/rest/v1/company_investor', params=params)
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, relations: list[dict]) -> list[dict]:
        if not relations:
            return []
        # Traer todas las relaciones existentes (asumiendo volumen bajo)
        existing = await supabase_client.get('/rest/v1/company_investor')
        existing_set = set((e['company_id'], e['investor_id']) for e in existing) if existing else set()
        to_insert = [rel for rel in relations if (rel['company_id'], rel['investor_id']) not in existing_set]
        inserted = []
        for rel in to_insert:
            data = {'company_id': rel['company_id'], 'investor_id': rel['investor_id']}
            res = await supabase_client.post('/rest/v1/company_investor', [data])
            inserted.append(res)
        return inserted 