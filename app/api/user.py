from libs.yellowPrint import YellowPrint

yp_user = YellowPrint('rp_user', url_prefix='/user')


@yp_user.route('/get')
def getuser():
    return 'this is getuser page'