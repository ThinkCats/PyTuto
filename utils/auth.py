from functools import wraps
from bottle import request, redirect
from utils.log import getLogger

logger = getLogger('auth')


def auth_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.get_cookie('account', secret='mysecret')
        if username is None:
            logger.info('auth check username None')
            redirect('/pp/login.html')
        else:
            logger.info('auth check username: %s' % username)
            return func(*args, **kwargs)
    return wrapper
