from libs.yellowPrint import YellowPrint

yp_book = YellowPrint('rp_user', url_prefix='/book')


@yp_book.route('/get')
def getbook():
    return 'this is getbook page'
