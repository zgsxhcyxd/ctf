
import memcache
from tornado.web import RequestHandler
from models.users import User


class BaseUserHandler(RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("user_id")
        user_obj = User.query.get(user_id)
        if user_obj is not None
            return user_obj
        return None


