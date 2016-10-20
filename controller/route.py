from bottle import view, static_file
from utils.log import getLogger
from service.articleservice import get_article_list, get_article_detail
from utils.db import Article
from utils.auth import auth_check
from utils.contexts import SingletonClass

app = SingletonClass().app
route = app.route
logger = getLogger(__name__)


@route('/')
@view('index')
def hello():
    name = 'world'
    article_list = get_article_list()
    return dict(title=name, articles=article_list)


@route('/article/<id>.html')
@view('article')
def article(id):
    logger.info('article id: %s' % id)
    article = get_article_detail(id)
    logger.info('article :%s' % article)
    return dict(title='hh', article=article)


@route('/new.html')
@view('post')
@auth_check
def new():
    return dict(title='xx')


@route('/pp/login.html')
@view('login')
def login_view():
    pass


# static file
@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./res')


