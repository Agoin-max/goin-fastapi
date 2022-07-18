# API基础路由

from fastapi import APIRouter

from api.login import login, select_sql_test, add_sql_test, select
from api.login import index
from api.view import test_redis_depends, test_redis, test_log, test_query

Api_Router = APIRouter(prefix="/api", tags=["API路由"])

# 路由 -> 逻辑函数
"""接口summary参数说明必须书写接口用途,若无,Code Review不允通过"""
Api_Router.get("/index", summary="测试接口")(index)
Api_Router.post("/login", summary="登陆测试接口")(login)
Api_Router.get("/select", summary="数据库查询测试", deprecated=True)(select_sql_test)
Api_Router.post("/add", summary="数据库新增测试", deprecated=True)(add_sql_test)
Api_Router.get("/redis/depends/set", summary="redis测试")(test_redis_depends)
Api_Router.get("/redis/state/set", summary="redis测试")(test_redis)
Api_Router.get("/logger/test", summary="日志测试")(test_log)
Api_Router.get("/token/test", summary="SQL测试")(select)

Api_Router.get("/query", summary="原生SQL测试")(test_query)