# tornade-celery-ssl
Send to rabbitmq via celery with ssl

First you should setup rabbitmq ssl according to https://www.rabbitmq.com/ssl.html

1.Start celery worker of proj:<br/>
celery worker -A proj -l INFO

2.Start tornado:<br/>
cd tcelery; python tornado_async.py
