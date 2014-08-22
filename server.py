# -*- coding: utf-8 -*-
__author__ = 'florije'

import tornado.ioloop
import tornado.web
from handler import MainHandler, ExampleHandler, GreetHandler

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)
define("mysql_user", default='root', help="mysql_user", type=str)
define("mysql_pass", default='903326', help="run on the given port", type=str)
define("mysql_host", default=8000, help="run on the given port", type=str)
define("mysql_db", default=8000, help="run on the given port", type=str)
define("mysql_poolsize", default=8000, help="run on the given port", type=str)
define("debug", default=8000, help="run on the given port", type=str)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/greet", GreetHandler),
    (r"/example", ExampleHandler)
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
