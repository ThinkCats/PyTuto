from bottle import route, run, view, static_file, error
from utils.log import getLogger
from service.userservice import addUser

logger = getLogger('app')


@route('/')
@view('index')
def hello():
    name = 'world'
    return dict(title=name)


@route('/article')
@view('article')
def article():
    return dict(title='hh')

@route('/post')
@view('post')
def post():
	return dict(title='xx')

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
