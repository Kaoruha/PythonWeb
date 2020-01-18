from sqlalchemy import Column, Integer, String, Date, Boolean
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.models.base import Base
from flask_login import UserMixin


class User(UserMixin, Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    _password = Column('password', String(128), nullable=False)
    image = Column(String(255))
    summary = Column(String(255), default='这个人很懒')
    birthday = Column(Date)
    phone = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    last_sign = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    permission = Column(Integer, default=1)

    # 密码Getter
    @property
    def password(self):
        return self._password

    # 密码哈希加密
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # Flask-login要求返回用户的ID
    def get_id(self):
        return self.id


# flask-login的用户获取
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
