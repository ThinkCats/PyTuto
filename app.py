from bottle import Bottle, default_app
from waitress import serve
from controller.route import app as AppView # 引入加载
from controller.api import app as Api # 引入加载
from utils.contexts import SingletonClass

App = SingletonClass().app
error = App.error

# error page
@error(404)
def error404(error):
    return '404 not found'


@error(500)
def error500(error):
    return 'server error'

if __name__ == '__main__':
    #serve(App,host='0.0.0.0',port=8000)
    App.run(host='localhost', port=8000, debug=True, reloader=True)
