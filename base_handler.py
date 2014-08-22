# -*- coding: utf-8 -*-
import tornado.web
from backend import Backend

__author__ = 'florije'


class BaseHandler(tornado.web.RequestHandler):
    @property
    def backend(self):
        return Backend.instance()