from fastapi import UploadFile
from app.persistence.repositories.dataset_repository import DatasetRepository

class DatasetService:
    def __init__(self, repository: DatasetRepository):
        self.repository = repository

    async def process_dataset_upload(self, file: UploadFile) -> dict:
        content = await file.read()
        rows = self.repository.parse_csv(content)
        # Aquí podrías agregar validaciones y transformaciones
        # Suponiendo que la tabla destino es 'company'
        result = await self.repository.bulk_insert('company', rows)
        return {'inserted': len(rows), 'result': result} 