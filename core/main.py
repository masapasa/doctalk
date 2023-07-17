import os

import pypandoc
import sentry_sdk
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from core.middlewares.cors import add_cors_middleware
from core.routes.api_key_routes import api_key_router
from core.routes.brain_routes import brain_router
from core.routes.chat_routes import chat_router
from core.routes.crawl_routes import crawl_router
from core.routes.explore_routes import explore_router
from core.routes.misc_routes import misc_router
from core.routes.subscription_routes import subscription_router
from core.routes.upload_routes import upload_router
from core.routes.user_routes import user_router
from core.logger import get_logger

logger = get_logger(__name__)

sentry_dsn = os.getenv("SENTRY_DSN")
if sentry_dsn:
    sentry_sdk.init(
        dsn=sentry_dsn,
        traces_sample_rate=1.0,
    )

app = FastAPI()

add_cors_middleware(app)


@app.on_event("startup")
async def startup_event():
    if not os.path.exists(pypandoc.get_pandoc_path()):
        pypandoc.download_pandoc()


app.include_router(brain_router)
app.include_router(chat_router)
app.include_router(crawl_router)
app.include_router(explore_router)
app.include_router(misc_router)
app.include_router(upload_router)
app.include_router(user_router)
app.include_router(api_key_router)
app.include_router(subscription_router)


@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
