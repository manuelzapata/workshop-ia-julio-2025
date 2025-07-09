from app.persistence.supabase_client import supabase_client
import csv
from typing import Any

class DatasetRepository:
    async def bulk_insert(self, table: str, rows: list[dict[str, Any]]):
        # Inserta múltiples filas en la tabla indicada usando la API REST de Supabase
        # Supabase recomienda usar el endpoint /rest/v1/{table} con método POST
        path = f'/rest/v1/{table}'
        return await supabase_client.post(path, data=rows)

    def parse_csv(self, file_content: bytes) -> list[dict[str, Any]]:
        # Parsea el contenido CSV y lo convierte en una lista de diccionarios
        decoded = file_content.decode('utf-8')
        reader = csv.DictReader(decoded.splitlines())
        return [row for row in reader] 