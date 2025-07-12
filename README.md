# workshop-ia-julio-2025

## Backend (FastAPI)

### Requisitos
- Python 3.11+
- venv

### Instalación y ejecución

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env  # Edita las variables según tu entorno
venv/bin/uvicorn app.main:app --reload
```

### Probar endpoint de salud

- [http://127.0.0.1:8000/api/v1/health](http://127.0.0.1:8000/api/v1/health)

### Estructura de carpetas

- `src/backend/api/` — Routers/endpoints
- `src/backend/services/` — Lógica de negocio
- `src/backend/persistence/` — Acceso a datos y Supabase
- `src/backend/core/` — Configuración y middlewares

### Variables de entorno

Ver `.env.sample` para los valores requeridos.

### Subir dataset de ejemplo vía curl

Puedes subir el dataset de ejemplo con el siguiente comando (ajusta el puerto si es necesario):

```bash
curl -X POST \
  -F "file=@/Users/manuel/dev/remotonow/workshop-ia-julio-2025/src/database/dataset.csv" \
  http://127.0.0.1:8000/api/v1/dataset/upload
```

---

## Pruebas automatizadas (testing)

Para ejecutar los tests del backend:

1. Activa el entorno virtual y asegúrate de tener instaladas las dependencias y pytest:

```bash
source venv/bin/activate
pip install -r requirements.txt
pip install pytest
```

2. Ejecuta las pruebas desde la raíz del proyecto:

```bash
PYTHONPATH=src/backend ./src/backend/venv/bin/python -m pytest src/backend/tests
```

Esto ejecutará todos los tests unitarios del backend y mostrará el resultado en consola.