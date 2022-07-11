# API基础路由

from fastapi import APIRouter

from api.login import login, select_sql_test, add_sql_test
from api.login import index
from api.test_redis import test_redis_depends, test_redis, test_log

Api_Router = APIRouter(prefix="/api", tags=["API路由"])

# 路由 -> 逻辑函数
"""接口summary参数说明必须书写接口用途,若无,Code Review不允通过"""
Api_Router.get("/index", summary="测试接口")(index)
Api_Router.post("/login", summary="登陆测试接口")(login)
Api_Router.get("/select", summary="数据库查询测试")(select_sql_test)
Api_Router.post("/add", summary="数据库新增测试")(add_sql_test)
Api_Router.get("/redis/depends/set", summary="redis测试")(test_redis_depends)
Api_Router.get("/redis/state/set", summary="redis测试")(test_redis)
Api_Router.get("/logger/test", summary="日志测试")(test_log)
