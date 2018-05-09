import memcache
import hashlib
import os

from tornado import ioloop
from tornado.httpserver import HTTPServer
from tornado.options import options, define
from tornado import web
from lib.captcha import CaptchaPIL

urls = [
    (r'/', LoginHandler),
    (r'/user/login', UserLoginHandler),
    (r'/captcha', )
]
def get_cookie_secret():
    return hashlib.md5(os.urandom(32)).hexdigest()

app = web.Application(
    urls,
    cookie_secret = get_cookie_secret(),
    xsrf_cookies=False,
    forbidden_url='/403',
    "login_url": "/login",
)

def start_server():
    server = HTTPServer(
        app, 
    )
    ioloop.IOLoop.instance().start()