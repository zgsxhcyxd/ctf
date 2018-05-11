from . import Model
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime, Enum
from .enums import TopicType

class Topic(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    categories = Column(Enum(TopicType), default=TopicType.MISE)
    name = Column(String(50), nullable=False)
    prompt = Column(String(100))
    desc = Column(String(200))
    user_fb = Column(Integer, ForeignKey("users.id"), primary_key=True)
    team_fb = Column(Integer, ForeignKey("teams.id"), primary_key=True)
    create_time = Column(DateTime, nullable=False, default=db.func.now())
    update_time = Column(DateTime, default=db.func.now(), onupdate=db.func.now())
