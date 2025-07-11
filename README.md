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
pip install pytest  # Para ejecutar las pruebas
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