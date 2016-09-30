from bottle import route, run, view


@route('/hello')
@view('index')
def hello():
    name = 'world'
    return dict(name=name)

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True, reloader=True)
