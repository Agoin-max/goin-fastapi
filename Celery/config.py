# Celery配置文件
from celery.schedules import crontab, timedelta

broker_url = "redis://127.0.0.1:6379/2"
# RabbitMQ作任务队列
# broker_url = "amqp://guest:guest@127.0.0.1:5672//"
# Redis任务执行结果存储
result_backend = "redis://127.0.0.1:6379/3"
timezone = 'Asia/Shanghai'

imports = [
    "Celery.tasks",  # 导入定时任务的py文件
]

beat_schedule = {
    "test": {
        "task": "Celery.tasks.crontab_func1",
        "schedule": timedelta(seconds=5),
        "args": ()
    },
}
