from fastapi import FastAPI, Request
import time

from app.core.config import get_settings
from app.core.logger import setup_logger
from app.api.v1.endpoints.health import router as health_router

settings = get_settings()
logger = setup_logger()

app = FastAPI(title=settings.service_name)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    logger.info(
        f"{request.method} {request.url.path} "
        f"Status: {response.status_code} "
        f"Time: {process_time:.4f}s"
    )

    return response


app.include_router(health_router, prefix="/api/v1")

logger.info("Application startup complete")