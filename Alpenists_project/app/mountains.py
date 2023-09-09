from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import LoginManager, login_user, logout_user, current_user
from functools import wraps
from models import Mountains

bp = Blueprint('mountains', __name__, url_prefix="/mountains")

@bp.route("/")
def index():
    all_mountains = Mountains.get_all_mountains()
    return render_template("mountains/index.html")
