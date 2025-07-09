from app.persistence.supabase_client import supabase_client

class MetricsRepository:
    async def get_all_companies(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company')

    async def get_all_revenues(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company', params={'select': 'revenue'})

    async def get_all_valuations(self) -> list[dict]:
        return await supabase_client.get('/rest/v1/company', params={'select': 'valuation'})

    async def get_general_metrics(self) -> dict:
        # Ejemplo: obtener conteo, suma y promedio de campos clave
        total_companies = await supabase_client.get('/rest/v1/company', params={'select': 'id'})
        total_revenue = await supabase_client.get('/rest/v1/company', params={'select': 'revenue'})
        average_valuation = await supabase_client.get('/rest/v1/company', params={'select': 'valuation'})
        # Aquí deberías agregar lógica para calcular los agregados
        return {
            'total_companies': len(total_companies),
            'total_revenue': sum([c.get('revenue', 0) or 0 for c in total_revenue]),
            'average_valuation': (sum([c.get('valuation', 0) or 0 for c in average_valuation]) / len(average_valuation)) if average_valuation else 0
        }

metrics_repository = MetricsRepository() 