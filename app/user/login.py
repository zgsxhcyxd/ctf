from base import BaseUserHandler
from models.enums import Const
from models.users import User

class UserLoginHandler(BaseUserHandler):

    def post(self):
        username = self.get_arguments("username")
        password = self.get_arguments("password")
        captcha = self.get_arguments("captcha")
        if captcha.upper() != self.get_cookie("caprcha").upper():
            return self.write({Const.RESULT_CODE: Const.STATUS_ERROR, Const.MESSAGE_KEY: "验证码错误!"})

        user = User.query.filter_by(username=username).first()
        if user is None:
            return self.write({Const.RESULT_CODE: Const.STATUS_ERROR, Const.MESSAGE_KEY: "当前用户不存在!"})
