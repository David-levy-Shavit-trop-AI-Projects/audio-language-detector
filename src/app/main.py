from fastapi import FastAPI
from src.app.core.config import settings
from src.app.core.logger import logger
from src.app.api.routes import router as api_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(api_router)

logger.info("App is running...")