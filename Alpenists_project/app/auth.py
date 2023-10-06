from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, current_user
from app import db
from models import Users
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix="/auth")

def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_user)

def load_user(user_id):
    user = db.session.execute(db.select(Users).filter_by(id=user_id)).scalar()
    return user

@bp.route('/login', methods=['GET', 'POST'])
def login():
    information = {}
    if request.method == 'POST':
        login = request.form.get('loginInput')
        password = request.form.get('passwordInput')
        information["login"] = login
        information["password"] = password
        remember_me = request.form.get('remember_me') == 'on'
        if login and password:
            user = db.session.execute(db.select(Users).filter_by(login=login)).scalar()
            if user and user.check_password(password):
                login_user(user, remember=remember_me)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('login.html', action="login", information=information)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@bp.route('/new_user', methods=['GET', 'POST'])
def new_user():
    information = {}
    if request.method == 'POST':
        login = request.form.get('loginInput')
        password = request.form.get('passwordInput')
        password_return = request.form.get('passwordInput_return')
        information["login"] = login
        information["password"] = password
        information["password_return"] = password_return
        if (Users.query.filter_by(login=login).all()):
            flash('Пользователь с таким логином уже существует.', 'danger')
            return render_template('login.html', action="create", information=information)
        if (password != password_return):
            flash('Пароли должны совпадать.', 'danger')
            return render_template('login.html', action="create", information=information)
        user = Users(login=login)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Пользователь успешно добавлен.', 'success')
        return redirect(url_for("index"))
    else:
        return render_template('login.html', action="create", information=information)
    
