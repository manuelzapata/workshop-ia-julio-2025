from app.persistence.supabase_client import supabase_client
import csv
from typing import Any
import re

COLUMN_MAP = {
    'Company Name': 'name',
    'Founded Year': 'founded_year',
    'Total Funding': 'total_funding',
    'ARR': 'arr',
    'Valuation': 'valuation',
    'Employees': 'employees',
    'G2 Rating': 'g2_rating',
}

# Solo columnas válidas para Supabase
VALID_COLUMNS = {
    'name', 'founded_year', 'total_funding', 'arr', 'valuation', 'employees', 'g2_rating', 'products'
}

def clean_money(value):
    if not value or value == 'N/A':
        return None
    value = value.replace('$', '').replace(',', '').strip()
    if value.endswith('B'):
        try:
            return float(value[:-1]) * 1_000_000_000
        except Exception:
            return None
    if value.endswith('M'):
        try:
            return float(value[:-1]) * 1_000_000
        except Exception:
            return None
    if value.endswith('K'):
        try:
            return float(value[:-1]) * 1_000
        except Exception:
            return None
    try:
        return float(value)
    except Exception:
        return None

def clean_int(value):
    if not value or value == 'N/A':
        return None
    try:
        return int(value.replace(',', ''))
    except Exception:
        return None

def clean_row(row):
    # Solo columnas válidas y limpieza de datos
    cleaned = {
        'name': row.get('name'),
        'founded_year': clean_int(row.get('founded_year')),
        'total_funding': clean_money(row.get('total_funding')),
        'arr': clean_money(row.get('arr')),
        'valuation': clean_money(row.get('valuation')),
        'employees': clean_int(row.get('employees')),
        'g2_rating': float(row.get('g2_rating')) if row.get('g2_rating') not in (None, '', 'N/A') else None,
    }
    # Procesar productos como lista JSON si existe
    if row.get('Product'):
        cleaned['products'] = [p.strip() for p in row['Product'].split(',')]
    return cleaned

def map_row(row):
    return {COLUMN_MAP.get(k, k): v for k, v in row.items()}

class DatasetRepository:
    async def bulk_insert(self, table: str, rows: list[dict[str, Any]]):
        # Mapear y limpiar columnas antes de enviar a Supabase
        mapped_rows = [map_row(row) for row in rows]
        cleaned_rows = [clean_row(row) for row in mapped_rows]
        print('DEBUG - Datos enviados a Supabase:', cleaned_rows)
        path = f'/rest/v1/{table}'
        return await supabase_client.post(path, cleaned_rows)

    def parse_csv(self, file_content: bytes) -> list[dict[str, Any]]:
        decoded = file_content.decode('utf-8')
        reader = csv.DictReader(decoded.splitlines())
        return [row for row in reader] 