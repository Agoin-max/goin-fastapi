from fastapi import Depends, Request

from core.Response import success
from curd.query import select_dict, select_list, sql_execute, get_pagination
from database.redis import sys_cache
from aioredis import Redis
from core.Logger import logger


# 方式一


async def test_redis_depends(today: int, cache: Redis = Depends(sys_cache)):
    # 连接池 - 依赖注入
    await cache.set("Goin", today, ex=300)
    print(111)
    return "ok"


# 方式二
async def test_redis(req: Request):
    # 连接池放在request
    value = await req.app.state.cache.get("Goin")
    return value


async def test_log():
    logger.info("日志测试")
    return success(msg="日志输出")


async def test_query():
    data = select_dict("select * from tbl_token_log where id=%s and ip=%s", params=(1, "124.204.40.42"), flat=True)

    sql = "insert into tbl_token_log (uid,created_at,ip,client,token) values (%s,%s,%s,%s,%s)"

    sql_execute(sql, params=(351, "2019-03-11 10:59:41", "1.202.218.58",
                             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)",
                             "1af1ffa35f1f6ee690c8a172937f2683"))
    res_data = select_list("select * from tbl_token_log")
    print(res_data)

    sql = "select * from tbl_token_log"
    tol_sql = "select count(id) as count from tbl_token_log"
    return success(data=get_pagination(sql, tol_sql))

    # return success(data=data)


from typing import TypeVar

T = TypeVar('T', bound = [str])


def func(value: T) -> T:
    return value


result = func("1")
print(result)