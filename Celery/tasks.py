from Celery.main import app


@app.task
def crontab_func1():
    print("测试1")
