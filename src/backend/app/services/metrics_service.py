from app.persistence.repositories.metrics_repository import MetricsRepository

class MetricsService:
    def __init__(self, repository: MetricsRepository):
        self.repository = repository

    async def get_general_metrics(self) -> dict:
        companies = await self.repository.get_all_companies()
        revenues = [c.get('revenue', 0) or 0 for c in companies]
        valuations = [c.get('valuation', 0) or 0 for c in companies]
        return {
            'total_companies': len(companies),
            'total_revenue': sum(revenues),
            'average_valuation': (sum(valuations) / len(valuations)) if valuations else 0
        } 