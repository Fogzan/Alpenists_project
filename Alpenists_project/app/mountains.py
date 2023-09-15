from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
from models import Mountains
from app import db

bp = Blueprint('mountains', __name__, url_prefix="/mountains")

@bp.route("/")
def index():
    mountains = Mountains.query.all()
    return render_template("mountains/index.html", mountains=mountains)

@bp.route("/new", methods=['GET', 'POST'])
def add_new():
    params = {}
    errors = {}
    if request.method == "POST":
        name = request.form.get('name')
        height_str = request.form.get('height')
        country = request.form.get('country')
        district = request.form.get('district')

        params['name'] = name
        params['height'] = height_str
        params['country'] = country
        params['district'] = district

        if  not name.isalpha():
            errors['name'] = "Название должно состоять только из букв (одно слово)."
        if not height_str.isdigit():
            errors['height'] = "Высота указывается в метрах (одно число)."
        else:
            height = int(height_str)
        if not country.isalpha():
            errors['country'] = "Страна должна состоять только из букв (одно слово)."
        if not district.isalpha():
            errors['district'] = "Окрестность должна состоять только из букв (одно слово)."

        if errors:
            return render_template("mountains/add_new.html", errors=errors, params=params)
        
        mountains = Mountains(name=name, height=height, coutry=country, district=district)
        db.session.add(mountains)
        db.session.commit()

        flash('Гора успешно добавлена.', 'success')
        return redirect(url_for('mountains.index'))


    return render_template("mountains/add_new.html", errors=errors, params=params)
