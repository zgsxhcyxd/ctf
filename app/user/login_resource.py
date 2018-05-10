from app.base import BaseUserHandler
from app.models.enums import Const
from app.models.users import User
from app.libs.utils import hash_user_password

class UserLoginHandler(BaseUserHandler):

    def post(self):
        username = self.get_arguments("username")
        password = self.get_arguments("password")
        # TODO 暂无第三方文件服务平台
        # captcha = self.get_arguments("captcha")
        # if captcha.upper() != self.get_cookie("caprcha").upper():
        #     return self.write({Const.RESULT_CODE: Const.STATUS_ERROR, Const.MESSAGE_KEY: "验证码错误!"})

        user = User.query.filter_by(username=username).first()
        if user is None:
            return self.write({Const.RESULT_CODE: Const.STATUS_ERROR, Const.MESSAGE_KEY: "当前用户不存在!"})

        if hash_user_password(username, password) != user.password:
            return self.write({Const.RESULT_CODE: Const.STATUS_ERROR, Const.MESSAGE_KEY: "您的用户名或者密码不正确!"})
        
        return self.write({Const.RESULT_CODE: Const.STATUS_OK , Const.MESSAGE_KEY: "验证成功"})
