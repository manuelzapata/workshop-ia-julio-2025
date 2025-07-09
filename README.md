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
venv/bin/uvicorn src.backend.main:app --reload
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