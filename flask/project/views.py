from flask import Blueprint

bp = Blueprint('principal',__name__,url_prefix='/')

@bp.route('/')
def principal():
    return "Flask is running"