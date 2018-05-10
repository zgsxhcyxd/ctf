from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.libs.datebase_connection import DatabaseConnection
from config import config

connection_database = DatabaseConnection(**config.mysql_configurations)

engine = create_engine(str(connection_database))
engine.dialect.supports_sane_rowcount =  False
engine.dialect.supports_sane_multi_rowcount = False
_Session = sessionmaker(bind=engine, expire_on_commit=False)
StartSession = lambda: _Session(autoflush=True)

dbsession = StartSession()

Model = declarative_base()