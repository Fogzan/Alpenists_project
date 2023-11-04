from os import getenv


class CONFIG():
    SECRET_KEY = getenv('SECRET_KEY')
    DB_NAME = getenv('MYSQL_DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_HOST")}:3306/{DB_NAME}'

class DEV_CONFIG():
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_DEV_HOST")}:3306/{getenv("MYSQL_DATABASE")}'
    MYSQL_ENGINE_URI = f'mysql+mysqlconnector://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_DEV_HOST")}:3306'

# Test for teamsity n6