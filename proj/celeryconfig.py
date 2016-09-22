from kombu import Queue
import ssl

MODULE_NAME = 'proj'

BROKER_URL = "amqp://guest:guest@localhost:5671//"

CELERY_RESULT_BACKEND = "amqp"

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

CELERY_IMPORTS=('proj.tasks', )
