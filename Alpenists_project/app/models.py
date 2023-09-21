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
        return Climbing.query.filter(Climbing.mountains_id == self.id).count()
    
    @property
    def get_count_climbes(self):
        count_res = 0
        climbings = Climbing.query.filter(Climbing.mountains_id == self.id).all()
        
        for climbing in climbings:
            count_res += Climbers.query.join(ClimbersGroups).filter(ClimbersGroups.group_id == climbing.group_id).count()
        return count_res


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

    @property
    def get_mountains_name(self):
        return Mountains.query.get(self.mountains_id).name
    
    @property
    def get_groups_name(self):
        return Groups.query.get(self.group_id).name
    
    @property
    def get_sostav_group(self):
            climbers = Climbers.query.join(ClimbersGroups).filter(ClimbersGroups.group_id == self.group_id).all()
            list_climber = []
            for climber in climbers:
                list_climber.append(climber.fio)
            return list_climber
    
    def get_sostav_group_cl(self):
            climbers = Climbers.query.join(ClimbersGroups).filter(ClimbersGroups.group_id == self.group_id).all()
            for climber in climbers:
                climber.dateStart = self.date_start
            return climbers
    