from fastapi import FastAPI
from app.api import health_router, dataset_router, metrics_router, company_router
from app.api.middleware import add_middlewares
from app.core.config import settings

app = FastAPI(title='SaaS Analytics API', version='0.1.0')
add_middlewares(app)
app.include_router(health_router, prefix=settings.api_prefix)
app.include_router(dataset_router, prefix=settings.api_prefix)
app.include_router(metrics_router, prefix=settings.api_prefix)
app.include_router(company_router, prefix=settings.api_prefix) 