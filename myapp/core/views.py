# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Accomplishment

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    accomplishments = Accomplishment.query.order_by(Accomplishment.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', accomplishments=accomplishments)

@core.route('/info')
def info():
    return render_template('info.html')