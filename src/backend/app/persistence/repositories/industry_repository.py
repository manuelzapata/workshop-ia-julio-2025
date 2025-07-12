from app.persistence.supabase_client import supabase_client

class IndustryRepository:
    async def get_by_name(self, name: str) -> dict | None:
        result = await supabase_client.get('/rest/v1/industry', params={'name': f'eq.{name}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, industries: list[str]) -> list[dict]:
        if not industries:
            return []
        # Consulta masiva de nombres existentes
        names_str = ','.join([f'"{name}"' for name in industries])
        params = {'name': f'in.({names_str})'}
        existing = await supabase_client.get('/rest/v1/industry', params=params)
        existing_names = set(e['name'] for e in existing) if existing else set()
        to_insert = [name for name in industries if name not in existing_names]
        inserted = []
        for name in to_insert:
            data = {'name': name}
            res = await supabase_client.post('/rest/v1/industry', [data])
            inserted.append(res)
        return inserted 