from bottle import route, run, view, static_file, error, post, request
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


@route('/new')
@view('post')
def new():
    return dict(title='xx')


@post('/post')
def post():
    title = request.forms.get('title')
    markdown = request.forms.get('test-editormd-markdown-doc')
    html = request.forms.get('test-editormd-html-code')
    article = Article()
    article.title = title
    article.markdown = markdown
    article.html = html
    add_article(article)
    return 'hhh'


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
    run(host='localhost', port=8000, debug=True, reloader=True)
