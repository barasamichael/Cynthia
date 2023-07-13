from flask import (render_template, flash, redirect, url_for, request, g, 
        jsonify, current_app)
from flask_login import current_user, login_required
from app import db
from app.models import User
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/upload_signature', methods=['GET', 'POST'])
@login_required
def upload_signature():
    return render_template('upload_signature.html')
