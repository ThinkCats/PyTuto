from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, Text,  ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import datetime

engine = create_engine('mysql://root:123456@127.0.0.1:3306/py_tuto?charset=utf8', echo=True)
Base = declarative_base()


@contextmanager
def sessionScope():
    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()
    session.expire_on_commit = False
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class User(Base):
    __tablename__ = 'user'

    id = Column('user_id', Integer, primary_key=True)
    name = Column(String(20))
    nickname = Column(String(20))
    password = Column(String(20))
    createTime = Column(DateTime,default=datetime.datetime.now)
    updateTime = Column(DateTime, onupdate=datetime.datetime.now)


class Article(Base):
    __tablename__ = 'article'

    id = Column('article_id', Integer, primary_key=True)
    title = Column(String(40))
    markdown = Column(String(6000))
    html = Column(Text)
    preview = Column(Text)
    createTime = Column(DateTime,default=datetime.datetime.now)
    updateTime = Column(DateTime, onupdate=datetime.datetime.now)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column('comment_id', Integer, primary_key=True)
    content = Column(String(500))
    createTime = Column(DateTime,default=datetime.datetime.now)
    updateTime = Column(DateTime, onupdate=datetime.datetime.now)


def init_db():
    Base.metadata.create_all(engine)
