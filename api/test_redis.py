from fastapi import Depends, Request

from core.Response import success
from database.redis import sys_cache
from aioredis import Redis
from core.Logger import logger


# 方式一
async def test_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # 连接池 - 依赖注入
    await cache.set("Goin", today, ex=300)
    return "ok"


# 方式二
async def test_redis(req: Request):
    # 连接池放在request
    value = await req.app.state.cache.get("Goin")
    return value


async def test_log():
    logger.info("日志测试")
    print(1/0)
    return success(msg="日志输出")


