from bottle import route, run, view, static_file, error
from db import Sessions

session = Sessions()

@route('/')
@view('index')
def hello():
    name = 'world'
#    session = Sessions()
    print('index session :', session.session)
    return dict(title=name)


@route('/article')
@view('article')
def article():
#    session = Sessions()
    print('article session :', session.session)
    return dict(title='hh')


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
