# 事件监听
from typing import Callable

from aioredis import Redis
from fastapi import FastAPI
from database.mysql import init_mysql
from database.redis import sys_cache


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        # APP启动完成后触发
        print("启动完毕")
        # 注册数据库
        await init_mysql(app)
        # await database.connect()
        # 缓存redis
        app.state.cache = await sys_cache()
    return app_start


def stopping(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        # APP停止时触发
        print("停止")
        # await database.disconnect()
        cache: Redis = await app.state.cache
        await cache.close()
    return stop_app
