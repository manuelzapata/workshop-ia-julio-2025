from fastapi import FastAPI
from src.backend.api import health_router
from src.backend.api.middleware import add_middlewares
from src.backend.core.config import settings

app = FastAPI(title='SaaS Analytics API', version='0.1.0')
add_middlewares(app)
app.include_router(health_router, prefix=settings.api_prefix)

@app.get('/health')
def health_check():
    return {'status': 'ok'} 