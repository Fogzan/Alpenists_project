from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required
from functools import wraps
from models import Climbing, Mountains, Groups
from app import db

bp = Blueprint('climbing', __name__, url_prefix="/climbing")

@bp.route("/")
@login_required
def index():
    climbings = Climbing.query.all()
    return render_template("climbing/index.html", climbings=climbings)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
def add_new():
    mountains = Mountains.query.all()
    groups = Groups.query.all()

    params = {}
    errors = {}
    if request.method == "POST":
        mountain = request.form.get('select-mountain')
        group = request.form.get('select-group')
        date_start = request.form.get('dateStart')
        date_end = request.form.get('dateEnd')

        params['date_start'] = date_start
        params['date_end'] = date_end

        if not mountain.isdigit():
            errors['mountain'] = "Выберете гору."
        else:
            params['mountain'] = int(mountain)

        if not group.isdigit():
            errors['group'] = "Выберете группу."
        else:
            params['group'] = int(group)

        if not date_start:
            errors['dateStart'] = "Выберете время начала."

        if not date_end:
            errors['dateEnd'] = "Выберете время окончания."

        if errors:
            return render_template("climbing/add_new.html", mountains=mountains, groups=groups, errors=errors, params=params, typeCreate="noGroup")
        
        сlimbing = Climbing(mountains_id=mountain, group_id=group, date_start=date_start, date_end=date_end)
        db.session.add(сlimbing)
        db.session.commit()

        flash('Восхождение успешно добавлено.', 'success')
        return redirect(url_for('climbing.index'))


    return render_template("climbing/add_new.html", mountains=mountains, groups=groups, errors=errors, params=params, typeCreate="noGroup")

@bp.route("/newAndGroup", methods=['GET', 'POST'])
@login_required
def add_new_2():
    mountains = Mountains.query.all()
    groups = Groups.query.all()

    params = {}
    errors = {}
    if request.method == "POST":
        group = request.form.get('name')

        mountain = request.form.get('select-mountain')
        date_start = request.form.get('dateStart')
        date_end = request.form.get('dateEnd')

        params['date_start'] = date_start
        params['date_end'] = date_end
        params['group'] = group

        if not mountain.isdigit():
            errors['mountain'] = "Выберете гору."
        else:
            params['mountain'] = int(mountain)

        if group == "":
            errors['group'] = "Введите название группы."

        if not date_start:
            errors['dateStart'] = "Выберете время начала."

        if not date_end:
            errors['dateEnd'] = "Выберете время окончания."

        if errors:
            return render_template("climbing/add_new.html", mountains=mountains, groups=groups, errors=errors, params=params, typeCreate="yesGroup")
        
        groups = Groups(name=group)
        db.session.add(groups)
        db.session.commit()

        сlimbing = Climbing(mountains_id=mountain, group_id=groups.id, date_start=date_start, date_end=date_end)
        db.session.add(сlimbing)
        db.session.commit()

        flash('Восхождение успешно добавлено.', 'success')
        return redirect(url_for('climbing.index'))


    return render_template("climbing/add_new.html", mountains=mountains, groups=groups, errors=errors, params=params, typeCreate="yesGroup")