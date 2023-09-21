from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required
from functools import wraps
from models import Climbers, Climbing, ClimbersGroups, Mountains, Groups
from app import db
import datetime

bp = Blueprint('climbers', __name__, url_prefix="/climbers")

@bp.route("/")
@login_required
def index():
    climbers = Climbers.query.all()
    return render_template("climbers/index.html", climbers=climbers)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
def add_new():
    params = {}
    errors = {}
    if request.method == "POST":
        fio = request.form.get('fio')
        address = request.form.get('address')

        params['fio'] = fio
        params['address'] = address

        fio_arr = fio.split()

        if len(fio_arr) != 3:
            errors['fio'] = "ФИО должно состоять из трех слов."

        for fio_arr_el in fio_arr:
            if  not fio_arr_el.isalpha():
                errors['fio'] = "ФИО должно состоять только из букв."
                break

        if errors:
            return render_template("climbers/add_new.html", errors=errors, params=params)
        
        climbers = Climbers(fio=fio, address=address)
        db.session.add(climbers)
        db.session.commit()

        flash('Альпенист успешно добавлен.', 'success')
        return redirect(url_for('climbers.index'))

    return render_template("climbers/add_new.html", errors=errors, params=params)

@bp.route("/<int:climber_id>/showStatistics")
@login_required
def show_stat(climber_id):
    groups = ClimbersGroups.query.filter(ClimbersGroups.climbers_id == climber_id).all()
    result = {}
    for group in groups:
        climbings = Climbing.query.filter(Climbing.group_id == group.group_id).all()
        print(">>>" + str(groups))
        for climbing in climbings:
            name = Mountains.query.get(climbing.mountains_id).name
            if name in result:
                result[name] += 1
            else:
                result[name] = 1

    climber_name = Climbers.query.get(climber_id).fio

    return render_template("climbers/show_stat.html", stats=result, climber_name=climber_name)

@bp.route("/showClimbers", methods=['GET', 'POST'])
@login_required
def show_climbers():
    climbers = Climbers.query.all()
    params = {}
    if request.method == "POST":
        date_start_str = request.form.get('dateStart')
        date_end_str = request.form.get('dateEnd')

        params["dateStart"] = date_start_str
        params["dateEnd"] = date_end_str

        if date_start_str:
            date_start = datetime.datetime.strptime(date_start_str, '%Y-%m-%dT%H:%M')
        else:
            date_start = datetime.datetime(1, 1, 1, 00, 00, 00)
        if date_end_str:
            date_end = datetime.datetime.strptime(date_end_str, '%Y-%m-%dT%H:%M')
        else:
            date_end = datetime.datetime(9999, 12, 30, 23, 59, 59)

        climbings = db.session.query(Climbing, ClimbersGroups, Climbers).join(ClimbersGroups, Climbing.group_id == ClimbersGroups.group_id).join(Climbers, Climbers.id == ClimbersGroups.climbers_id).all()

        results = []
        for climbing in climbings:
            if (climbing.Climbing.date_start >= date_start) and (climbing.Climbing.date_end <= date_end):
                results.append({
                    "id": climbing.Climbers.id,
                    "fio": climbing.Climbers.fio,
                    "address": climbing.Climbers.address,
                })

        itog_results = []
        for result in results:
            flag = 0
            for itog_result in itog_results:
                if result["id"] == itog_result["id"]:
                    flag = 1
                    break
            if flag == 0:
                itog_results.append(result)

        
        return render_template("climbers/show_climbers.html", climbers=itog_results, params=params)

    return render_template("climbers/show_climbers.html", climbers=climbers)

