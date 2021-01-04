from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    #url_for 안에 question._list 는 .앞의 question은 블루프린터이고
    #_list는 블루프린터 내에 함수를 말한다.
