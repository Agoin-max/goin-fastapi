from celery import Celery

app = Celery("Nebula")

app.config_from_object("Celery.config")
