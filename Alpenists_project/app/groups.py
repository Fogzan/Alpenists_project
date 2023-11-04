from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required
from functools import wraps
from models import Groups, Climbers, ClimbersGroups, Climbing
from app import db
import datetime

bp = Blueprint('groups', __name__, url_prefix="/groups")

@bp.route("/")
@login_required
def index():
    groups = Groups.query.all()

    for group in groups:
        climbers = Climbers.query.join(ClimbersGroups).filter(ClimbersGroups.group_id == group.id).all()
        list_climber = []
        for climber in climbers:
            list_climber.append(climber.fio)
        group.climbers = list_climber
    
    return render_template("groups/index.html", groups=groups)

@bp.route("/new", methods=['GET', 'POST'])
@login_required
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

@bp.route("/<int:group_id>/addClimbers", methods=['GET', 'POST'])
@login_required
def add_climbers(group_id):
    group_name = Groups.query.get(group_id).name
    climbers = Climbers.query.all()
    errors = {}
    if request.method == "POST":
        climber = request.form.get('select-climbers')

        if not climber.isdigit():
            errors['climber'] = "Выберете альпиниста."

        climbers_groups = ClimbersGroups.query.filter(ClimbersGroups.climbers_id == climber, ClimbersGroups.group_id == group_id).all()

        if climbers_groups:
            errors['climber'] = "Такой альпинист уже есть в этой группе."

        if errors:
            return render_template("groups/add_new_climber.html", errors=errors, climbers=climbers, groupName=group_name)
        
        climbers_groups = ClimbersGroups(climbers_id=climber, group_id=group_id)
        db.session.add(climbers_groups)
        db.session.commit()

        flash('Альпинист успешно добавлен к группе.', 'success')
        return redirect(url_for('groups.index'))


    return render_template("groups/add_new_climber.html", errors=errors, climbers=climbers, groupName=group_name)


@bp.route("/showGroup", methods=['GET', 'POST'])
@login_required
def show_group():
    groups = Groups.query.all()
    params = {}
    if request.method == "POST":
        date_start_str = request.form.get('dateStart')
        date_end_str = request.form.get('dateEnd')


        if date_start_str:
            date_start = datetime.datetime.strptime(date_start_str, '%Y-%m-%dT%H:%M')
        else:
            date_start = datetime.datetime(1, 1, 1, 00, 00, 00)
        if date_end_str:
            date_end = datetime.datetime.strptime(date_end_str, '%Y-%m-%dT%H:%M')
        else:
            date_end = datetime.datetime(9999, 12, 30, 23, 59, 59)

        params["dateStart"] = date_start_str
        params["dateEnd"] = date_end_str

        results = []
        
        groups = db.session.query(Climbing, Groups).join(Groups).all()

        for group in groups:
            if (group.Climbing.date_start >= date_start) and (group.Climbing.date_end <= date_end):
                climbers = Climbers.query.join(ClimbersGroups).filter(ClimbersGroups.group_id == group.Groups.id).all()
                list_climber = []
                for climber in climbers:
                    list_climber.append(climber.fio)
                print(">>>>")
                print(group.Groups.id)
                results.append({
                    "id": group.Groups.id,
                    "name": group.Groups.name,
                    "climbers": list_climber
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
        
        return render_template("groups/show_group.html", groups=itog_results, params=params)

    return render_template("groups/show_group.html", groups=groups)
