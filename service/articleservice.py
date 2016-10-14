from utils.db import Article, sessionScope
from sqlalchemy import desc
from collections import defaultdict


def add_article(article):
    with sessionScope() as session:
        session.add(article)

def get_article_detail(id):
    with sessionScope() as session:
        return session.query(Article).filter(Article.id == id).first()

def get_article_list():
    with sessionScope() as session:
        result= defaultdict(list)
        article_list = session.query(Article).order_by(desc(Article.createTime)).all()
        for article in article_list:
            create_time = article.createTime
            year_ = create_time.year
            result[year_].append(article)
        return result.items()
