from app.persistence.supabase_client import supabase_client

class IndustryRepository:
    async def get_by_name(self, name: str) -> dict | None:
        result = await supabase_client.get('/rest/v1/industry', params={'name': f'eq.{name}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, industries: list[str]) -> list[dict]:
        # Insertar solo las industrias que no existen
        inserted = []
        for name in industries:
            existing = await self.get_by_name(name)
            if not existing:
                data = {'name': name}
                res = await supabase_client.post('/rest/v1/industry', [data])
                inserted.append(res)
        return inserted 