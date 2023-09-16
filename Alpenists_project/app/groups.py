from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
from models import Groups
from app import db

bp = Blueprint('groups', __name__, url_prefix="/groups")

@bp.route("/")
def index():
    groups = Groups.query.all()
    return render_template("groups/index.html", groups=groups)

@bp.route("/new", methods=['GET', 'POST'])
def add_new():
    params = {}
    errors = {}
    if request.method == "POST":
        name = request.form.get('name')

        params['name'] = name

        if name == "":
            errors['name'] = "Введите название."

        if errors:
            return render_template("groups/add_new.html", errors=errors, params=params)
        
        groups = Groups(name=name)
        db.session.add(groups)
        db.session.commit()

        flash('Группа успешно добавлена.', 'success')
        return redirect(url_for('groups.index'))


    return render_template("groups/add_new.html", errors=errors, params=params)
