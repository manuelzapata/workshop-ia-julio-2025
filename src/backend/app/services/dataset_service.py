from fastapi import UploadFile

def process_dataset_upload(file: UploadFile) -> dict:
    # Aquí iría la lógica real de procesamiento y guardado en la base de datos
    # Por ahora, solo retorna el nombre del archivo
    return {'filename': file.filename} 