# -*- coding: utf-8 -*-
# @Time    : 2018/05/07 下午1:20
# @Author  : Jake
# @Desc    : 基类设计
# @File    : __init__.py

import memcache
from tornado.web import RequestHandler
from app.models.users import User
from config import config
from app.models import dbsession

class BaseUserHandler(RequestHandler):
    db_session = dbsession
    _memcached = None

    def get_current_user(self):
        user_id = self.get_secure_cookie("user_id")
        user_obj = User.query.get(user_id)
        if user_obj is not None:
            return user_obj
        return None

    def memcached(self):
        if self._memcached is None:
            self._memcached = memcache.Client(**config.memcached, debug=0)


