from flask import Blueprint
# 蓝图
bp_user = Blueprint('bp_user', __name__, url_prefix="/user")
bp_details = Blueprint('bp_details', __name__)
