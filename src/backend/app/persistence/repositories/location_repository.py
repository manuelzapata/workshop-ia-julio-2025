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
        inserted = []
        for loc in locations:
            city = loc['city']
            state_province = loc.get('state_province')
            country = loc['country']
            existing = await self.get_by_fields(city, state_province, country)
            if not existing:
                data = {'city': city, 'state_province': state_province, 'country': country}
                res = await supabase_client.post('/rest/v1/location', [data])
                inserted.append(res)
        return inserted 