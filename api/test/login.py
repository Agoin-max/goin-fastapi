from typing import List
from pydantic import BaseModel
from models.base import User


class Login(BaseModel):
    username: str
    password: str


def index(age: int):
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


async def select():
    pass
    # _token = await Token().all()
    # print(_token)
    # # data = {
    # #     "uid": 90,
    # #     "token": "c5d984cdd671d6506b66fff15f9226ab",
    # #     "ip": "1.202.218.58",
    # #     "client_md5": "b4046c447614e06d949fe3062a42a"
    # # }
    # # await Token().create(**data)
    # _token_log = await TokenLog().all()
    # print(_token_log)
    # return _token


