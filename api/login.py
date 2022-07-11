from typing import List
from pydantic import BaseModel

from core.Exception import TestException
from models.base import User


class Login(BaseModel):
    username: str
    password: str


def index(age: int):
    print(1/0)
    return {"func": "test", "age": age}


def login(data: Login):
    if data.username == "Goin":
        raise TestException()
    return data


# 数据查询Test
async def select_sql_test():
    _user = await User().all()
    print(_user)
    return _user


# 数据新增Test
async def add_sql_test(data: Login):
    await User().create(**{"username": data.username, "password": data.password})
    return "ok"
