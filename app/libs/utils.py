# -*- coding: utf-8 -*-
# @Time    : 2018/05/10 下午4:31
# @Author  : Jake
# @Desc    : 工具类
# @File    : utils.py

def hash_user_password(username, password):
    import hashlib
    sha256 = hashlib.sha256()
    sha256.update(username.encode('utf-8'))
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()