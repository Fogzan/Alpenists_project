from os import getenv
from dotenv import load_dotenv
load_dotenv('.env' if getenv('ENV') == 'production' else '../.env')

class CONFIG():
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{getenv("MYSQL_USER")}:{getenv("MYSQL_PASSWORD")}@{getenv("MYSQL_HOST")}:3306/{getenv("MYSQL_DATABASE")}'

# Test for teamsity n6