# 应用初始化

from flask import Flask

from app import setting, secure
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(secure)
    app.config.from_object(setting)
    reg_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    return app


# 将所有需要蓝图引入并注册
def reg_blueprint(app):
    from app.user.user import bp_user
    app.register_blueprint(bp_user)
    from app.web.details_page import bp_details
    app.register_blueprint(bp_details)
