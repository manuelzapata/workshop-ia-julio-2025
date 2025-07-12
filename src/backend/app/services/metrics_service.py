from app.persistence.repositories.metrics_repository import MetricsRepository
from app.utils.location_formatter import format_location

class MetricsService:
    def __init__(self, repository: MetricsRepository):
        self.repository = repository

    async def get_general_metrics(self) -> dict:
        companies = await self.repository.get_all_companies()
        # Use 'arr' field for revenue (Annual Recurring Revenue)
        revenues = [c.get('arr', 0) or 0 for c in companies]
        valuations = [c.get('valuation', 0) or 0 for c in companies]
        
        # Count funding rounds (companies with total_funding > 0)
        funding_rounds = sum(1 for c in companies if (c.get('total_funding', 0) or 0) > 0)
        
        # Get top location by counting companies per location
        location_counts = {}
        for company in companies:
            location_id = company.get('location_id')
            if location_id:
                location_counts[location_id] = location_counts.get(location_id, 0) + 1
        
        top_location = None
        top_location_count = 0
        
        if location_counts:
            # Find the location with the most companies
            top_location_id = max(location_counts, key=location_counts.get)
            top_location_count = location_counts[top_location_id]
            
            # Get location details
            locations = await self.repository.get_all_locations()
            for loc in locations:
                if loc.get('id') == top_location_id:
                    top_location = format_location(loc)
                    break
        
        return {
            'total_companies': len(companies),
            'total_revenue': sum(revenues),
            'average_valuation': (sum(valuations) / len(valuations)) if valuations else 0,
            'funding_rounds': funding_rounds,
            'top_location': {
                'name': top_location,
                'companies': top_location_count
            }
        } 