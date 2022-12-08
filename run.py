# app运行文件

import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from tortoise.exceptions import DoesNotExist, OperationalError

from config import settings
from fastapi.staticfiles import StaticFiles
from core.Router import all_router
from core.Events import startup, stopping
from core.Exception import http_error_handler, http422_error_handler, unicorn_exception_handler, UnicornException, \
    mysql_does_not_exist, mysql_operational_error
from core.Middleware import Middleware
import uvicorn
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

app = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME,
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# 事件监听
app.add_event_handler("startup", startup(app))
app.add_event_handler("shutdown", stopping(app))

# 异常错误处理
app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(RequestValidationError, http422_error_handler)
app.add_exception_handler(UnicornException, unicorn_exception_handler)
app.add_exception_handler(DoesNotExist, mysql_does_not_exist)
app.add_exception_handler(OperationalError, mysql_operational_error)

# 异常日志sentry收集
SentryAsgiMiddleware(app)

# 路由
app.include_router(all_router)

# 中间件
app.add_middleware(Middleware)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

# 静态资源目录
app.mount("/static", StaticFiles(directory=os.path.join(os.getcwd(), "static")))

if __name__ == '__main__':
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True, workers=1)
