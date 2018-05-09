from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from libs.database_connection import DatabaseConnection
from config import config

connection_database = DatabaseConnection(**config.mysql_configurations)

engine = create_engine(connection_database)
engine.dialect.supports_sane_rowcount =  False
engine.dialect.supports_sane_multi_rowcount = False
_Session = sessionmaker(bind=engine, expire_on_commit=False)
StartSession = lambda: _Session(autoflush=True)

dbsession = StartSession()

Model = declarative_base()