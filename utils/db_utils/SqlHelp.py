import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.ext.declarative import declarative_base

from API.GlobalParameters import global_settings


# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    global_settings.db_connect_str
)
SessionLocal = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()








if __name__ == '__main__':
    # db=get_db()
    # fileProjectInfo = db.query(FileProjectInfo).filter_by(MD5Value="md5value").first()
    # create_all_tables()
    pass