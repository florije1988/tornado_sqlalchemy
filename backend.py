# -*- coding: utf-8 -*-
__author__ = 'florije'

from sqlalchemy.orm import sessionmaker
from tornado.options import options
from sqlalchemy import create_engine


class Backend(object):
    def __init__(self):
        engine = create_engine(
            "mysql://{0}:{1}@{2}/{3}".format(options.mysql_user, options.mysql_pass, options.mysql_host,
                                             options.mysql_db)
            , pool_size=options.mysql_poolsize
            , pool_recycle=3600
            , echo=options.debug
            , echo_pool=options.debug)
        self._session = sessionmaker(bind=engine)

    @classmethod
    def instance(cls):
        """Singleton like accessor to instantiate backend object"""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def get_session(self):
        return self._session()