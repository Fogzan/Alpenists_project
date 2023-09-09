import os
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import current_app
from app import db


# Горы
class Mountains(db.Model):
    __tablename__ = 'mountains'

    id = db.Column(db.Integer, primery_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.Integer)
    coutry = db.Column(db.String(100))
    district = db.Column(db.String(100))

def get_all_mountains(self):
        return Mountains.query.all()


# Альпенисты
class Climbers(db.Model):
    __tablename__ = 'climbers'

    id = db.Column(db.Integer, primery_key=True)
    fio = db.Column(db.String(100))
    address = db.column(db.String(100))
    

# Связь авльпенистов и групп (много ко многим)
class ClimbersGroups(db.Model):
    __tablename__ = 'climbers_groups'

    id = db.Column(db.Integer, primery_key=True)
    climbers_id = db.Column(db.Integer, db.Climbers('climbers.id'))
    group_id = db.Column(db.Integer, db.Groups('groups.id'))
    

# Группы
class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primery_key=True)
    name = db.Column(db.String(100))


# Восхождения
class Climbing(db.Model):
    __tablename__ = 'climbings'

    id = db.Column(db.Integer, primery_key=True)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    mountains_id = db.Column(db.Integer, db.Mountains('mountains.id'))
    group_id = db.Column(db.Integer, db.Groups('groups.id'))
