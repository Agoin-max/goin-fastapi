# API基础路由

from fastapi import APIRouter

from api.test.login import select_sql_test, add_sql_test, select
from api.test.login import index
from api.test.view import test_redis_depends, test_redis, test_log, test_query

api_router = APIRouter(prefix="/api")

# 路由 -> 逻辑函数
api_router.get("/index", summary="测试接口")(index)
# api_router.post("/login", summary="登陆测试接口")(login)
api_router.get("/select", summary="数据库查询测试", deprecated=True)(select_sql_test)
api_router.post("/add", summary="数据库新增测试", deprecated=True)(add_sql_test)
api_router.get("/redis/depends/set", summary="redis测试")(test_redis_depends)
api_router.get("/redis/state/set", summary="redis测试")(test_redis)
api_router.get("/logger/test", summary="日志测试")(test_log)
api_router.get("/token/test", summary="SQL测试")(select)

api_router.get("/query", summary="原生SQL测试")(test_query)