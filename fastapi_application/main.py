import logging
from fastapi import FastAPI, HTTPException
import uvicorn

from fastapi_application.core.config import settings
from fastapi_application.api import router as api_router

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="FastAPI Application",
    description="Basic FastAPI Application",
    version="1.0.0"
)

app.include_router(api_router, prefix=settings.api.prefix)

# Подключаем роутер
try:
    app.include_router(api_router, prefix=settings.api.prefix)
    logger.info(f"API router подключен с префиксом {settings.api.prefix}")
except Exception as e:
    logger.error(f"Ошибка при подключении роутера: {str(e)}")
    raise

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Глобальная ошибка: {str(exc)}")
    return {"error": str(exc)}

if __name__ == "__main__":
    try:
        logger.info(f"Запуск сервера на {settings.run.host}:{settings.run.port}")
        uvicorn.run(
            "main:app",
            host=settings.run.host,
            port=settings.run.port,
            reload=True,
            log_level="info"
        )
    except Exception as e:
        logger.error(f"Ошибка при запуске сервера: {str(e)}")
        raise


