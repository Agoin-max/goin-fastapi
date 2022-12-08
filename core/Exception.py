# 异常处理
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from tortoise.exceptions import OperationalError, DoesNotExist


async def http_error_handler(_: Request, exc: HTTPException):
    # http异常处理
    return JSONResponse({
        "code": exc.status_code,
        "message": exc.detail,
        "data": exc.detail,
    },
        status_code=exc.status_code)


class UnicornException(Exception):

    def __init__(self, code, message, data=None):
        if not data:
            data = {}
        self.code = code
        self.message = message
        self.data = data


async def unicorn_exception_handler(_: Request, exc: UnicornException):
    return JSONResponse({
        "code": exc.code,
        "message": exc.message,
        "data": exc.data,
    })


async def http422_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError]) -> JSONResponse:
    return JSONResponse({
        "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "message": f"参数校验错误{exc.errors()}",
        "data": exc.errors(),
    },
        status_code=422
    )


async def mysql_operational_error(_: Request, exc: OperationalError):
    print("OperationalError", exc)
    return JSONResponse({
        "code": -1,
        "message": "服务端错误",
        "data": []
    }, status_code=500)


async def mysql_does_not_exist(_: Request, exc: DoesNotExist):
    print("DoesNotExist", exc)
    return JSONResponse({
        "code": -1,
        "message": "发出的请求针对的是不存在的记录,服务器没有进行操作",
        "data": []
    }, status_code=404)


# 自定义异常 -> 友好提示 -> 异常扩展写法(示例)
class UserException(UnicornException):

    def __init__(self, data=None, message=""):
        if not data:
            data = {}
        self.code = 10001
        self.message = message
        self.data = data
