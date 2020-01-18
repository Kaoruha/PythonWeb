from app.blueprints import bp_details


@bp_details.route('/tech1', methods=['GET', 'POST'])
def getinfo():
    return '<h1>This is Details Page!</h1>'
