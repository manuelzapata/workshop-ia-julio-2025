from app.persistence.supabase_client import supabase_client

class InvestorRepository:
    async def get_by_name(self, name: str) -> dict | None:
        result = await supabase_client.get('/rest/v1/investor', params={'name': f'eq.{name}'})
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, investors: list[str]) -> list[dict]:
        if not investors:
            return []
        
        # Get all existing investors first (assuming low volume)
        existing = await supabase_client.get('/rest/v1/investor')
        existing_names = set(e['name'] for e in existing) if existing else set()
        
        # Filter out existing investors
        to_insert = [name for name in investors if name not in existing_names]
        
        if not to_insert:
            return []
        
        # Bulk insert all new investors at once
        data = [{'name': name} for name in to_insert]
        try:
            result = await supabase_client.post('/rest/v1/investor', data)
            return result if isinstance(result, list) else [result]
        except Exception as e:
            # Log error and handle appropriately
            raise Exception(f"Failed to bulk insert investors: {e}") 