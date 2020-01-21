# 应用初始化
from flask import Flask
from config import secure, setting
from models.base import db


# 将所有插件引入并注册
def reg_plugins(app):
    # 数据库
    db.init_app(app)
    with app.app_context():
        db.create_all()


# 注册蓝图
def reg_blueprints(app):
    from app.api import create_blueprint
    app.register_blueprint(create_blueprint())


def create_app():
    app = Flask(__name__)

    # 加载配置文件
    app.config.from_object(secure)
    app.config.from_object(setting)

    # 注册蓝图
    reg_blueprints(app)

    return app
