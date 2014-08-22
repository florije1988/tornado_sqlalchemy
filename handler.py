# -*- coding: utf-8 -*-
from base_handler import BaseHandler

__author__ = 'florije'


class ExampleHandler(BaseHandler):
    def get(self):
        session = self.backend.get_session()
        try:
            """Everything I need to do here"""

            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()


class GreetHandler(BaseHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")