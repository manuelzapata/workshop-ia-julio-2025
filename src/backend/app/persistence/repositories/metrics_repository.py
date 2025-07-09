from app.persistence.supabase_client import supabase_client

class MetricsRepository:
    async def get_all_companies(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company')

    async def get_all_revenues(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company', params={'select': 'revenue'})

    async def get_all_valuations(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company', params={'select': 'valuation'})

# No se instancia aquí, la instancia se hace en el servicio o por inyección de dependencias 