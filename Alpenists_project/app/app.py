from flask import Flask, render_template, session, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from sqlalchemy import MetaData, create_engine, text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import getenv, environ
from config import CONFIG

from prometheus_client import generate_latest
from prometheus_client import Counter
from prometheus_client import Summary

app = Flask(__name__)

# Create a metric to track time spent and requests made.
INDEX_TIME = Summary('index_request_processing_seconds', 'DESC: INDEX time spent processing request')

# Create a metric to count the number of runs on process_request()
c = Counter('requests_for_host', 'Number of runs of the process_request method', ['method', 'endpoint'])

application = app
load_dotenv('.env' if getenv('ENV') == 'production' else '../.env')
app.config.from_object(CONFIG)


# Работа с БД
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
# print(environ)
print(app.config)

# Создание базы данных при первичном запуске
with create_engine(app.config['MYSQL_ENGINE_URI']).connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {app.config['DB_NAME']}"))

migrate = Migrate(app, db)

from models import create_models
# create_models(app)
# ---------------------------

from mountains import bp as mountains_bp
app.register_blueprint(mountains_bp)
from climbers import bp as climbers_bp
app.register_blueprint(climbers_bp)
from climbing import bp as climbing_bp
app.register_blueprint(climbing_bp)
from groups import bp as groups_bp
app.register_blueprint(groups_bp)
from auth import bp as auth_bp, init_login_manager
app.register_blueprint(auth_bp)
init_login_manager(app)

@app.route('/')
@INDEX_TIME.time()
def index():
    path = str(request.path)
    verb = request.method
    label_dict = {"method": verb,
                 "endpoint": path}
    c.labels(**label_dict).inc()
    return render_template('index.html')

@app.route('/test')
@INDEX_TIME.time()
def test():
    path = str(request.path)
    verb = request.method
    label_dict = {"method": verb,
                 "endpoint": path}
    c.labels(**label_dict).inc()
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    return generate_latest()





# что не так!?