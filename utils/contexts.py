from bottle import Bottle


def singleton(cls):
    instances = {}

    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getInstance


@singleton
class SingletonClass:

    def __init__(self):
        self.app = Bottle()
