from fastapi import UploadFile
from app.persistence.repositories.dataset_repository import DatasetRepository, map_row
from app.persistence.repositories.industry_repository import IndustryRepository
from app.persistence.repositories.location_repository import LocationRepository
from app.persistence.repositories.investor_repository import InvestorRepository
from app.persistence.repositories.company_investor_repository import CompanyInvestorRepository
from app.persistence.repositories.company_repository import CompanyRepository

class DatasetService:
    def __init__(self, repository: DatasetRepository):
        self.repository = repository
        self.industry_repo = IndustryRepository()
        self.location_repo = LocationRepository()
        self.investor_repo = InvestorRepository()
        self.company_repo = CompanyRepository()
        self.company_investor_repo = CompanyInvestorRepository()

    async def process_dataset_upload(self, file: UploadFile) -> dict:
        print('Iniciando carga de dataset...')
        content = await file.read()
        rows = self.repository.parse_csv(content)
        print(f'Filas leídas del CSV: {len(rows)}')

        industries = self._extract_unique_industries(rows)
        print(f'Industrias únicas detectadas: {len(industries)}')
        await self._bulk_insert_industries(industries)
        print('Industrias insertadas.')

        locations = self._extract_unique_locations(rows)
        print(f'Ubicaciones únicas detectadas: {len(locations)}')
        await self._bulk_insert_locations(locations)
        print('Ubicaciones insertadas.')

        investors = self._extract_unique_investors(rows)
        print(f'Inversionistas únicos detectados: {len(investors)}')
        await self._bulk_insert_investors(investors)
        print('Inversionistas insertados.')

        industry_map = await self._map_industries_to_ids(industries)
        location_map = await self._map_locations_to_ids(locations)
        print('Mapeo de ids de industria y ubicación listo.')

        companies_to_insert = self._prepare_companies(rows, industry_map, location_map)
        print(f'Empresas a insertar: {len(companies_to_insert)}')
        result = await self.repository.bulk_insert('company', companies_to_insert)
        print('Empresas insertadas.')

        company_name_to_id = await self._map_company_names_to_ids(companies_to_insert)
        print('Mapeo de ids de empresas listo.')

        relations = await self._prepare_company_investor_relations(rows, company_name_to_id)
        print(f'Relaciones company_investor a insertar: {len(relations)}')
        await self._bulk_insert_company_investors(relations)
        print('Relaciones company_investor insertadas.')
        return {'inserted': len(rows), 'result': result}

    def _normalize(self, value: str) -> str:
        return value.strip().lower() if value else ''

    def _parse_hq(self, hq_string: str | None) -> tuple[str, str | None, str] | None:
        if not hq_string:
            return None

        parts = [p.strip() for p in hq_string.split(',')]
        city, state_province, country = None, None, None

        if len(parts) == 3:
            city, state_province, country = parts
        elif len(parts) == 2:
            city, country = parts
            state_province = None
        else:
            return None

        if not city or not country:
            return None

        return (
            self._normalize(city),
            self._normalize(state_province) if state_province else None,
            self._normalize(country)
        )

    def _extract_unique_industries(self, rows: list[dict]) -> dict[str, str]:
        """Retorna un diccionario {normalized_name: original_name}"""
        industry_map = {}
        for row in rows:
            if 'Industry' in row and row['Industry']:
                original = row['Industry'].strip()
                normalized = self._normalize(original)
                if normalized and normalized not in industry_map:
                    industry_map[normalized] = original
        return industry_map

    def _extract_unique_locations(self, rows: list[dict]) -> dict[tuple[str, str | None, str], tuple[str, str | None, str]]:
        """Retorna un diccionario {normalized_location: original_location}"""
        location_map = {}
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
                
                if not city or not country:
                    continue
                
                normalized_key = (
                    self._normalize(city),
                    self._normalize(state_province) if state_province else None,
                    self._normalize(country)
                )
                original_value = (city, state_province, country)
                
                if normalized_key not in location_map:
                    location_map[normalized_key] = original_value
        return location_map

    def _extract_unique_investors(self, rows: list[dict]) -> dict[str, str]:
        """Retorna un diccionario {normalized_name: original_name}"""
        investor_map = {}
        for row in rows:
            if 'Top Investors' in row and row['Top Investors']:
                for inv in row['Top Investors'].split(','):
                    original = inv.strip()
                    normalized = self._normalize(original)
                    if normalized and normalized not in investor_map:
                        investor_map[normalized] = original
        return investor_map

    async def _bulk_insert_industries(self, industries: dict[str, str]) -> None:
        # Insertar usando los nombres originales
        await self.industry_repo.bulk_insert(list(industries.values()))

    async def _bulk_insert_locations(self, locations: dict[tuple[str, str | None, str], tuple[str, str | None, str]]) -> None:
        # Insertar usando los nombres originales
        await self.location_repo.bulk_insert([
            {'city': city, 'state_province': state_province, 'country': country}
            for city, state_province, country in locations.values()
        ])

    async def _bulk_insert_investors(self, investors: dict[str, str]) -> None:
        # Insertar usando los nombres originales
        await self.investor_repo.bulk_insert(list(investors.values()))

    async def _map_industries_to_ids(self, industries: dict[str, str]) -> dict:
        industry_map = {}
        for normalized_name, original_name in industries.items():
            obj = await self.industry_repo.get_by_name(original_name)
            if obj:
                industry_map[normalized_name] = obj['id']
        return industry_map

    async def _map_locations_to_ids(self, locations: dict[tuple[str, str | None, str], tuple[str, str | None, str]]) -> dict:
        location_map = {}
        for normalized_location, original_location in locations.items():
            city, state_province, country = original_location
            obj = await self.location_repo.get_by_fields(city, state_province, country)
            if obj:
                location_map[normalized_location] = obj['id']
        return location_map

    def _prepare_companies(self, rows: list[dict], industry_map: dict, location_map: dict) -> list[dict]:
        companies = []
        for i, row in enumerate(rows):
            company = map_row(row)
            
            industry_name = self._normalize(row.get('Industry', ''))
            company['industry_id'] = industry_map.get(industry_name)

            parsed_location = self._parse_hq(row.get('HQ'))
            if parsed_location:
                company['location_id'] = location_map.get(parsed_location)
            else:
                company['location_id'] = None

            companies.append(company)
        return companies

    async def _map_company_names_to_ids(self, companies: list[dict]) -> dict:
        company_name_to_id = {}
        for company in companies:
            company_obj = await self.company_repo.get_by_name(company['name'])
            if company_obj:
                company_name_to_id[company['name']] = company_obj['id']
        return company_name_to_id

    async def _prepare_company_investor_relations(self, rows: list[dict], company_name_to_id: dict) -> list[dict]:
        relations = []
        for row in rows:
            company_id = company_name_to_id.get(row.get('Company Name', '').strip())
            if not company_id:
                continue
            if 'Top Investors' in row and row['Top Investors']:
                for inv in row['Top Investors'].split(','):
                    original_investor_name = inv.strip()
                    investor_obj = await self.investor_repo.get_by_name(original_investor_name)
                    if investor_obj:
                        relations.append({'company_id': company_id, 'investor_id': investor_obj['id']})
        return relations

    async def _bulk_insert_company_investors(self, relations: list[dict]) -> None:
        await self.company_investor_repo.bulk_insert(relations) 