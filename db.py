from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456@127.0.0.1:3306/py_tuto', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Sessions:

    def __init__(self):
        self.session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column('user_id', Integer, primary_key=True)
    name = Column(String(20))
    nickname = Column(String(20))
    password = Column(String(20))
    createTime = Column(DateTime)
    updateTime = Column(DateTime)


class Article(Base):
    __tablename__ = 'article'

    id = Column('article_id', Integer, primary_key=True)
    title = Column(String(20))
    content = Column(String(5000))
    createTime = Column(DateTime)
    updateTime = Column(DateTime)


class Comment(Base):
    __tablename__ = 'comment'

    id = Column('comment_id', Integer, primary_key=True)
    content = Column(String(500))
    createTime = Column(DateTime)
    updateTime = Column(DateTime)


# Base.metadata.create_all(engine)
