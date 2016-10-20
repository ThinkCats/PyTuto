from bottle import Bottle,request,response,redirect
from utils.log import getLogger
from utils.db import Article
from service.userservice import addUser
from service.articleservice import add_article

app = Bottle()
route = app.route
logger = getLogger(__name__)

@route('/login',method='post')
def login():
    form_value = request.POST.decode('utf-8')
    username = form_value.get('username')
    password = form_value.get('password')
    logger.info('username: %s,password: %s' % (username, password))
    response.set_cookie('account', username, secret='mysecret',max_age=600)
    redirect('/new.html')


@route('/post',method='post')
def post():
    form_value = request.POST.decode('utf-8')
    title = form_value.get('title')
    markdown = form_value.get('content-markdown-doc')
    html = form_value.get('content-html-code')
    preview = form_value.get('preview-html')
    article = Article()
    article.title = title
    article.markdown = markdown
    article.html = html
    article.preview = preview
    add_article(article)
    redirect('/')


@route('/add')
def add():
    addUser()
    return 'add ok'


