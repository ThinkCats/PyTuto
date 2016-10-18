from bottle import route, run, view, static_file, error, post, request, redirect, default_app
from paste import httpserver
from utils.log import getLogger
from service.userservice import addUser
from service.articleservice import add_article, get_article_list, get_article_detail
from utils.db import Article

logger = getLogger('app')


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
def new():
    return dict(title='xx')


@post('/post')
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


# static file
@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root='./res')


# error page
@error(404)
def error404(error):
    return '404 not found'


@error(500)
def error500(error):
    return 'server error'

if __name__ == '__main__':
    application = default_app()
    httpserver.serve(application,host='0.0.0.0',port=8000)
    ##run(host='localhost', port=8000)
