import pymysql
import os


# 创建数据库的链接
class MysqlConnection:

    def __init__(self):
        self.kwargs = {
            "user": os.getenv("BASE_USER", "admin"),
            "password": os.getenv("BASE_PASSWORD", "atZPTRWa86KczsSPnUyY"),
            "host": os.getenv("BASE_HOST", "nebula-database.cectwbqueqym.rds.cn-north-1.amazonaws.com.cn"),
            "database": os.getenv("BASE_DB", "nebula.site"),
            "port": int(os.getenv("BASE_PORT", 3306)),
            "charset": "utf8mb4"
        }

    # 完成链接数据库
    def connect(self):
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()
        return self.db, self.cur

    # 关闭
    def close(self):
        self.cur.close()
        self.db.close()
