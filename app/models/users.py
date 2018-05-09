from models import Model
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import DateTime, Integer, String, Boolean, Enum
from models.enums import Area, TeamPermission

class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    username = Column(String(20), unique=True)
    password = Column(String(64), nullable=False)
    # 禁止登录
    active = Column(Boolean, nullable=False, default=True)
    # 最后一次登录
    last_login = Column(DateTime)
    # 分值
    score = Column(Integer, default=0)
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def verify_password(self, password):
        new_pwd = hash_user_password(self.email, password, current_app.config['STARTUP_SALT'])
        return self.password == new_pwd


class Team(Model):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    _name = Column(String(20), unique=True, nullable=False)
    company_name = Column(String(20))
    score = Column(Integer, default=0)
    area = Column(Enum(Area), , default=Area.BJ)
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class UserTeam(Model):
    __tablename__ = 'user_team'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), primary_key=True)
    permissions = db.Column(db.Enum(TeamPermission), default=TeamPermission.MEMBER)
    create_time = Column(DateTime, nullable=False, default=datetime.now())
    update_time = Column(DateTime, default=datetime.now(), onupdate=datetime.now())