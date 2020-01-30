from flask_httpauth import HTTPBasicAuth
from libs.error_code import APIException

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
    pass
