from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required
from functools import wraps
from models import Mountains, Groups, ClimbersGroups, Climbers, Climbing
from app import db

bp = Blueprint('mountains', __name__, url_prefix="/mountains")

@bp.route("/")
@login_required
def index():
    mountains = Mountains.query.all()
    return render_template("mountains/index.html", mountains=mountains)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
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

@bp.route("/<int:mountain_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_mouintain(mountain_id):
    params = {}
    errors = {}
    mountain = Mountains.query.get(mountain_id)
    if request.method == "GET":
        params = mountain

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
        
        mountain.name = name
        mountain.height = height
        mountain.coutry = country
        mountain.district = district
        
        db.session.commit()

        flash('Гора успешно изменена.', 'success')
        return redirect(url_for('mountains.index'))

    return render_template("mountains/add_new.html", errors=errors, params=params)

@bp.route("/<int:mountain_id>/grops")
@login_required
def show_groups(mountain_id):
    mountain_name = Mountains.query.get(mountain_id).name

    climbings = Climbing.query.filter(Climbing.mountains_id == mountain_id).order_by(Climbing.date_start).all()
    
    return render_template("mountains/groups.html", climbings=climbings, mountainName=mountain_name)
