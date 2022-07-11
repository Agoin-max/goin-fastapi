# 工具箱
import hashlib
import uuid

from passlib.handlers.pbkdf2 import pbkdf2_sha256


def random_str():
    # 唯一字符串
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding="UTF-8")).hexdigest()
    return str(only)


def encry_password(psw: str):
    # 密码加密
    return pbkdf2_sha256.hash(psw)


def check_password(password: str, old: str):
    # 密码校验
    check = pbkdf2_sha256.verify(password, old)
    if check:
        return True
    else:
        return False
