from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logger import setup_logger
from app.api.v1.endpoints.health import router as health_router

settings = get_settings()
logger = setup_logger()

app = FastAPI(title=settings.service_name)

app.include_router(health_router, prefix="/api/v1")

logger.info("Application startup complete")