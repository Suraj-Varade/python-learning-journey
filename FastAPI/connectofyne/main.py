import logging
from contextlib import asynccontextmanager

# middleware
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi.exception_handlers import http_exception_handler

from connectofyne.database import database
from connectofyne.logging_conf import configure_logging
from connectofyne.routers.file import router as file_router
from connectofyne.routers.post import router as post_router
from connectofyne.routers.user import router as user_router
from fastapi import FastAPI, HTTPException

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    logger.info("hello world")
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)

app.add_middleware(CorrelationIdMiddleware)  ## middleware

app.include_router(post_router, prefix="/api")
app.include_router(user_router, prefix="/api")
app.include_router(file_router, prefix="/api")


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exec):
    logging.error(f"HTTPException : {exec.status_code}, {exec.detail}")
    return await http_exception_handler(request, exec)
