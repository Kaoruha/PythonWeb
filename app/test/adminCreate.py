from app.models.base import db
from app.models.user import User

with db.auto_commit():
    admin = User()
    admin.name = 'superadmin'
    admin.password = 'caonima123'
    admin.is_active = True
    db.session.add(User)