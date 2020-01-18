from flask import make_response

from app.models.base import db
from app.models.user import User


# 设置Cookie
def set_cookie():
    response = make_response('Hello, Mr 7')
    response.set_cookie('name', 'Mr 7 ', 100)
    return response


# 数据库提交
def user_add():
    try:
        user = User()  # 生成模型类
        # 设置user属性
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


# 数据库提交高级版本
def user_add():
    with db.auto_commit(): # models.base里拓展了上下文方法
        user = User()  # 生成模型类
        # 设置user属性
        db.session.add(user)
