from models import Model
from sqlalchemy import Column
from collections import namedtuple
from sqlalchemy.types import DateTime, Integer, String, Boolean, BigInteger

class Role(Model):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(20))
    desc = db.Column(String(50))
    permission_key = db.Column(String(100), nullable=False, default="Admin")
    permissions = db.Column(BigInteger, nullable=False, default=0)
    status = db.Column(Boolean, default=True)
    create_time = Column(DateTime, nullable=False, default=db.func.now())
    update_time = Column(DateTime, default=db.func.now(), onupdate=db.func.now())


class Admin(Model):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True)
    password = Column(String(64), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    create_time = Column(DateTime, nullable=False, default=db.func.now())
    update_time = Column(DateTime, default=db.func.now(), onupdate=db.func.now())

class EnumEx(object):
    
    def __init__(self, **kwargs):
        self.data = dict()
        for key, value in kwargs.items():
            self.data[key] = namedtuple(key, value.keys())(*value.values())

    def __getattribute__(self):
        return self.data.get(key, None)

    def get(self):
        return self.data.get(key, None)


PERMISSION_DATA = {
    "Admin": {'name': '操作员管理', 'description': '最高级别操作员', 'value': 1 << 12},
    "User": {"name": "普通用户", "description": "普通用户", "value": 1 << 0}
}

permissions = EnumEx(**PERMISSION_DATA)