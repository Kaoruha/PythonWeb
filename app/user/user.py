from app.blueprints import bp_user


@bp_user.route('/login', methods=['GET', 'POST'])
def login():
    return '<h1>Login Page</h1>'


@bp_user.route('/register', methods=['GET', 'POST'])
def register():
    return '<h1>Register Page</h1>'
