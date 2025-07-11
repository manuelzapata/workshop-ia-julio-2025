from fastapi import UploadFile
from app.persistence.repositories.dataset_repository import DatasetRepository
from app.persistence.repositories.industry_repository import IndustryRepository
from app.persistence.repositories.location_repository import LocationRepository
from app.persistence.repositories.investor_repository import InvestorRepository
from app.persistence.repositories.company_investor_repository import CompanyInvestorRepository

class DatasetService:
    def __init__(self, repository: DatasetRepository):
        self.repository = repository

    async def process_dataset_upload(self, file: UploadFile) -> dict:
        print('Iniciando carga de dataset...')
        content = await file.read()
        rows = self.repository.parse_csv(content)
        print(f'Filas leídas del CSV: {len(rows)}')
        # INDUSTRY
        industries = set()
        for row in rows:
            if 'Industry' in row and row['Industry']:
                industries.add(row['Industry'].strip())
        print(f'Industrias únicas detectadas: {len(industries)}')
        industry_repo = IndustryRepository()
        await industry_repo.bulk_insert(list(industries))
        print('Industrias insertadas.')
        # LOCATION
        locations = set()
        for row in rows:
            if 'HQ' in row and row['HQ']:
                parts = [p.strip() for p in row['HQ'].split(',')]
                if len(parts) == 3:
                    city, state_province, country = parts
                elif len(parts) == 2:
                    city, country = parts
                    state_province = None
                else:
                    continue
                locations.add((city, state_province, country))
        print(f'Ubicaciones únicas detectadas: {len(locations)}')
        location_repo = LocationRepository()
        await location_repo.bulk_insert([
            {'city': city, 'state_province': state_province, 'country': country}
            for city, state_province, country in locations
        ])
        print('Ubicaciones insertadas.')
        # INVESTOR
        investors = set()
        for row in rows:
            if 'Top Investors' in row and row['Top Investors']:
                for inv in row['Top Investors'].split(','):
                    name = inv.strip()
                    if name:
                        investors.add(name)
        print(f'Inversionistas únicos detectados: {len(investors)}')
        investor_repo = InvestorRepository()
        await investor_repo.bulk_insert(list(investors))
        print('Inversionistas insertados.')
        # Poblar company (requiere industry_id y location_id)
        # Mapear industry/location a id
        industry_map = {}
        for name in industries:
            obj = await industry_repo.get_by_name(name)
            if obj:
                industry_map[name] = obj['id']
        location_map = {}
        for city, state_province, country in locations:
            obj = await location_repo.get_by_fields(city, state_province, country)
            if obj:
                location_map[(city, state_province, country)] = obj['id']
        print('Mapeo de ids de industria y ubicación listo.')
        # Insertar companies con los ids correctos
        companies_to_insert = []
        company_name_to_id = {}
        for row in rows:
            company = self.repository.map_row(row)
            # INDUSTRY
            industry_name = row.get('Industry', '').strip()
            company['industry_id'] = industry_map.get(industry_name)
            # LOCATION
            hq = row.get('HQ', '')
            parts = [p.strip() for p in hq.split(',')] if hq else []
            if len(parts) == 3:
                city, state_province, country = parts
            elif len(parts) == 2:
                city, country = parts
                state_province = None
            else:
                city = state_province = country = None
            company['location_id'] = location_map.get((city, state_province, country))
            companies_to_insert.append(company)
        print(f'Empresas a insertar: {len(companies_to_insert)}')
        result = await self.repository.bulk_insert('company', companies_to_insert)
        print('Empresas insertadas.')
        # Mapear company name a id
        for company in companies_to_insert:
            company_obj = await self.repository.supabase_client.get('/rest/v1/company', params={'name': f"eq.{company['name']}"})
            if company_obj and isinstance(company_obj, list) and len(company_obj) > 0:
                company_name_to_id[company['name']] = company_obj[0]['id']
        print('Mapeo de ids de empresas listo.')
        # Poblar company_investor
        company_investor_repo = CompanyInvestorRepository()
        relations = []
        for row in rows:
            company_id = company_name_to_id.get(row.get('Company Name', '').strip())
            if not company_id:
                continue
            if 'Top Investors' in row and row['Top Investors']:
                for inv in row['Top Investors'].split(','):
                    investor_name = inv.strip()
                    investor_obj = await investor_repo.get_by_name(investor_name)
                    if investor_obj:
                        relations.append({'company_id': company_id, 'investor_id': investor_obj['id']})
        print(f'Relaciones company_investor a insertar: {len(relations)}')
        await company_investor_repo.bulk_insert(relations)
        print('Relaciones company_investor insertadas.')
        return {'inserted': len(rows), 'result': result} 