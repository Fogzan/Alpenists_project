import os
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from flask import current_app
from app import db


# Пользователи
class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



# Горы
class Mountains(db.Model):
    __tablename__ = 'mountains'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    coutry = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100))

    def get_all_mountains(self):
        return Mountains.query.all()
    
    @property
    def get_count_climbing(self):
        return Climbing.query.filte(Climbing.mountains_id == self.id).count()


# Альпенисты
class Climbers(db.Model):
    __tablename__ = 'climbers'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    

# Связь авльпенистов и групп (много ко многим)
class ClimbersGroups(db.Model):
    __tablename__ = 'climbers_groups'

    id = db.Column(db.Integer, primary_key=True)
    climbers_id = db.Column(db.Integer, db.ForeignKey('climbers.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    

# Группы
class Groups(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


# Восхождения
class Climbing(db.Model):
    __tablename__ = 'climbings'

    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)
    mountains_id = db.Column(db.Integer, db.ForeignKey('mountains.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
