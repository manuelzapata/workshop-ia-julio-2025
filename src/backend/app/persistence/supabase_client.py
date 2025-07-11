import httpx
from app.core.config import settings

class SupabaseClient:
    def __init__(self):
        self.base_url = settings.supabase_url
        self.api_key = settings.supabase_key
        self.headers = {
            'apikey': self.api_key,
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }
        self.client = httpx.AsyncClient()

    async def get(self, path: str, params: dict = None):
        url = f'{self.base_url}{path}'
        response = await self.client.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    async def post(self, path: str, data: dict = None):
        url = f'{self.base_url}{path}'
        headers = self.headers.copy()
        headers['Prefer'] = 'return=representation'
        response = await self.client.post(url, headers=headers, json=data)
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError:
            print('SUPABASE ERROR:', response.text)
            raise
        try:
            return response.json()
        except Exception:
            print('SUPABASE NON-JSON RESPONSE:', response.text)
            return {'error': 'Non-JSON response', 'content': response.text, 'status_code': response.status_code}

supabase_client = SupabaseClient() 