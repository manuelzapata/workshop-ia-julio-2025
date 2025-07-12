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
        
        # Get all existing industries first (assuming low volume)
        existing = await supabase_client.get('/rest/v1/industry')
        existing_names = set(e['name'] for e in existing) if existing else set()
        
        # Filter out existing industries
        to_insert = [name for name in industries if name not in existing_names]
        
        if not to_insert:
            return []
        
        # Bulk insert all new industries at once
        data = [{'name': name} for name in to_insert]
        try:
            result = await supabase_client.post('/rest/v1/industry', data)
            return result if isinstance(result, list) else [result]
        except Exception as e:
            # Log error and handle appropriately
            raise Exception(f"Failed to bulk insert industries: {e}") 