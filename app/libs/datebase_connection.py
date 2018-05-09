import logging
import os
from sqlalchemy import create_engine
from tornado.options import options

class DatabaseConnection(object):

    def __init__(self, database, host=None, port=None, username=None, password=None, dialect=None):
        self.database = database
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dialect = dialect

    def __str__(self):
        if self.dialect == 'sqlist':
            db_conn = self._sqlite()
        elif self.dialect == 'postgres':
            db_conn = self._postgres()
        elif self.dialect == 'mysql':
            db_conn = self._mysql()
        self._test_connection(db_conn)
        return db_conn

    def _test_connection(self, connection_url):
        try:
            engine = create_engine(connection_url)
            connection = engine.connect()
            connection.close()
            return True
        except:
            if options.debug:
                logging.exception("Database connection failed")
            return False

    def _sqlite(self):
        logging.debug("Configured to use SQLite for a database")
        db_name = self.database
        if not len(db_name):
            db_name = 'rtb'
        return 'sqlite:///%s.db' % db_name

    def _mysql(self):
        logging.debug("Configured to use MySQL for a database")
         __mysql = 'mysql://%s:%s@%s/%s' % (
            self.username, self.password, self.host, self.database
        )
        __pymysql = 'mysql+pymysql://%s:%s@%s/%s' % (
            self.username, self.password, self.host, self.database
        )
        if self._test_connection(__mysql):
            return __mysql
        elif self._test_connection(__pymysql):
            return __pymysql
        else:
            logging.fatal("Connection can't to database with any available dirver")
            os._exit(1)

    def _postgres(self):
        logging.debug("Configured to use Postgresql for a database")
        try:
            import pypostgresql
        except ImportError:
            print(WARN + "You must install 'pypostgresql'")
            os._exit(1)
        postgres = 'postgresql+pypostgresql://%s:%s@%s/%s' % (
            self.username, self.password, self.host, self.database,
        )
        if self._test_connection(postgres):
            return postgres
        else:
            logging.fatal("Cannot connect to database with any available driver")
            os._exit(1)