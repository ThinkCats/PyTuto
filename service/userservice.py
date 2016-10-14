from utils.db import User, sessionScope


def addUser():
    with sessionScope() as session:
        user = User()
        user.name = '哈哈'
        user.nickname = '什么呢'
        user.password = 'ddddd'
        session.add(user)
