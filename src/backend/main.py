from fastapi import FastAPI
from api import health_router
from api.middleware import add_middlewares
from core.config import settings

app = FastAPI(title='SaaS Analytics API', version='0.1.0')
add_middlewares(app)
app.include_router(health_router, prefix=settings.api_prefix) 