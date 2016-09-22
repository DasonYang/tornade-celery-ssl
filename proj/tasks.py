from __future__ import absolute_import

from proj.celery import app

@app.task(name='tasks.on_receive')
def on_receive(reqs):
    print reqs
    return '200 OK.'