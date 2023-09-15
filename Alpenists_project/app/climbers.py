from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
from models import Climbers
from app import db

bp = Blueprint('climbers', __name__, url_prefix="/climbers")

@bp.route("/")
def index():
    climbers = Climbers.query.all()
    return render_template("climbers/index.html", climbers=climbers)

@bp.route("/new", methods=['GET', 'POST'])
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
