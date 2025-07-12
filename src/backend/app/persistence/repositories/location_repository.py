from app.persistence.supabase_client import supabase_client

class LocationRepository:
    async def get_by_fields(self, city: str, state_province: str | None, country: str) -> dict | None:
        params = {'city': f'eq.{city}', 'country': f'eq.{country}'}
        if state_province:
            params['state_province'] = f'eq.{state_province}'
        result = await supabase_client.get('/rest/v1/location', params=params)
        if result and isinstance(result, list) and len(result) > 0:
            return result[0]
        return None

    async def bulk_insert(self, locations: list[dict]) -> list[dict]:
        if not locations:
            return []
        # Traer todas las ubicaciones existentes (asumiendo volumen bajo)
        existing = await supabase_client.get('/rest/v1/location')
        existing_set = set((e['city'], e.get('state_province'), e['country']) for e in existing) if existing else set()
        to_insert = [loc for loc in locations if (loc['city'], loc.get('state_province'), loc['country']) not in existing_set]
        if not to_insert:
            return []
        
        # Bulk insert all new locations at once
        data = [
            {
                'city': loc['city'],
                'state_province': loc.get('state_province'),
                'country': loc['country']
            }
            for loc in to_insert
        ]
        try:
            result = await supabase_client.post('/rest/v1/location', data)
            return result if isinstance(result, list) else [result]
        except Exception as e:
            # Log error and handle appropriately
            raise Exception(f"Failed to bulk insert locations: {e}") 