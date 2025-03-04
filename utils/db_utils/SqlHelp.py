import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy.ext.declarative import declarative_base
from utils.config_util import CONFIG
from src.SystemSettings import Project_Path


SQLALCHEMY_DATABASE_URL =os.path.join(Project_Path,config_data["sqlListPath"])
# SQLALCHEMY_DATABASE_URL="E:\PythonProject\FileVisualization\data\database\sqllitedb\sqllitedb.db"
# print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(
    "sqlite:///"+SQLALCHEMY_DATABASE_URL
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