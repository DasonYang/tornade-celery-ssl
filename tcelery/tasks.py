import os
import time
from datetime import datetime

from celery import Celery


celery = Celery("tasks")
celery.config_from_object('celeryconfig')

@celery.task(name='tasks.on_receive')
def on_receive(reqs):
    print reqs
    return '200 OK.'

if __name__ == "__main__":
    celery.start()