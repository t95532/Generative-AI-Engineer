from fastapi import FastAPI
from app.core.config import get_settings
from app.core.logger import setup_logger

settings = get_settings()
logger = setup_logger()

app = FastAPI(title=settings.service_name)


@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message": f"{settings.service_name} Running"}