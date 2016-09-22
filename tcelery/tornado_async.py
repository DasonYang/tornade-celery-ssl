from tornado import gen
from tornado import ioloop
from tornado.web import asynchronous, RequestHandler, Application

import tasks

import tcelery
tcelery.setup_nonblocking_producer()

class MainHandler(RequestHandler):
    @asynchronous
    @gen.coroutine
    def get(self):
        response = yield gen.Task(tasks.on_receive.apply_async, args=[{'ip':'127.0.0.1'}])
        self.write(str(response.result))
        self.finish()

application = Application([
    (r"/hello", MainHandler),
])


if __name__ == "__main__":
    application.listen(8801)
ioloop.IOLoop.instance().start()