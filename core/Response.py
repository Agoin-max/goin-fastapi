# 响应类型
from typing import List


def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(data=None, msg=''):
    """成功返回格式"""
    return base_response(0, msg, data)


def fail(code=1, msg='', data=None):
    """失败返回格式"""
    return base_response(code, msg, data)


def total_result(data: List = None, total: int = 0, code: int = 0, page: int = 1, pagesize: int = 10, msg: str = ''):
    """
    支持total-design-table 返回的格式
    :param code:w
    :param data:
    :param total:
    :return:
    """
    if data is None:
        data = []
    return {
        "code": code,
        "data": data,
        "message": msg,
        "total": total,
        "page": page,
        "pagesize": pagesize
    }
