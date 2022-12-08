# 基本配置文件
import os.path
import secrets
from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings
from typing import List
import sentry_sdk


class Config(BaseSettings):
    # 加载环境变量
    load_dotenv(find_dotenv(), override=True)
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    PROJECT_NAME: str = "FastAPI"
    DESCRIPTION: str = "FastAPI"
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    # 跨域请求
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']
    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60  # session过期时间14天
    # Sentry
    sentry_sdk.init(
        dsn="https://0ed4f09a829d4a00aa3780fe1f4d175e@o1172746.ingest.sentry.io/6559988",

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
    )
    # Jwt
    JWT_SECRET_KEY = secrets.token_urlsafe(32)
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL = "/api/v1/admin/access/token"


settings = Config()
