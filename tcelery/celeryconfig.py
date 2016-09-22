#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssl
from urllib import urlencode
import pika

BROKER_URL = "amqp://guest:guest@127.0.0.1:5671//"

CELERY_RESULT_BACKEND = 'amqp://'

CELERY_DEFAULT_EXCHANGE = 'celery'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_QUEUE = 'celery'
CELERY_DEFAULT_ROUTING_KEY = 'celery'
CELERY_CREATE_MISSING_QUEUES = True
CELERY_TASK_RESULT_EXPIRES = 3600

BROKER_USE_SSL = {
    'ca_certs': '/etc/rabbitmq/ssl/certs/cacert.pem',
    'keyfile': '/etc/rabbitmq/ssl/certs/client_key.pem',
    'certfile': '/etc/rabbitmq/ssl/certs/client_cert.pem',
    'cert_reqs': ssl.CERT_REQUIRED
}

CELERYT_PIKA_OPTIONS = {
                    'ssl': True,
                    'ssl_options': dict(
                        ca_certs='/etc/rabbitmq/ssl/certs/cacert.pem',
                        keyfile='/etc/rabbitmq/ssl/certs/client_key.pem',
                        certfile='/etc/rabbitmq/ssl/certs/client_cert.pem',
                        cert_reqs=ssl.CERT_REQUIRED)
}