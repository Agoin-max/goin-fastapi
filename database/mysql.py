from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os

INSTALLED_APPS = [
    "models.base"
]

DB_ORM_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",
            "credentials": {
                "host": os.getenv("BASE_HOST", "nebula-database.cectwbqueqym.rds.cn-north-1.amazonaws.com.cn"),
                "user": os.getenv("BASE_USER", "admin"),
                "password": os.getenv("BASE_PASSWORD", "atZPTRWa86KczsSPnUyY"),
                "port": int(os.getenv("BASE_PORT", 3306)),
                "database": os.getenv("BASE_DB", "nebula.site"),
            }
        },
        # "db2": {
        #     "engine": "tortoise.backends.mysql",
        #     "creadentials": {
        #         "host": os.getenv("BASE_HOST", "127.0.0.1"),
        #         "user": os.getenv("BASE_USER", "root"),
        #         "password": os.getenv("BASE_PASSWORD", "12345678"),
        #         "port": int(os.getenv("BASE_PORT", 3306)),
        #         "database": os.getenv("BASE_DB", "base"),
        #     }
        # },
        # "db3": {
        #     "engine": "tortoise.backends.mysql",
        #     "creadentials": {
        #         "host": os.getenv("BASE_HOST", "127.0.0.1"),
        #         "user": os.getenv("BASE_USER", "root"),
        #         "password": os.getenv("BASE_PASSWORD", "12345678"),
        #         "port": int(os.getenv("BASE_PORT", 3306)),
        #         "database": os.getenv("BASE_DB", "base"),
        #     }
        # }
    },
    "apps": {
        "base": {"models": INSTALLED_APPS, "default_connection": "default"},
        # "db2": {"models": ["models.db2"], "default_connection": "db2"},
        # "db3": {"models": ["models.db3"], "default_connection": "db3"},
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}


async def init_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=False,  # 如果数据库为空,则自动生成对应表单,生产环境不要开
        add_exception_handlers=True  # 生产环境不要开,会泄露调试信息
    )
