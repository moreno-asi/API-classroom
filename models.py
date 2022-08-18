from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Classroom(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100),unique = True)
    capacity = db.Column(db.Integer)
    alumns = db.relationship('Alumn',backref='classroom',lazy=True)

    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity

class Alumn(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    surnames = db.Column(db.String(100))
    date_of_birth = db.Column(db.DateTime())
    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))

    def __init__(self,name,surnames,classroom_id,date_of_birth):
        self.name = name
        self.surnames = surnames
        self.classroom_id = classroom_id
        self.date_of_birth = datetime.strptime(date_of_birth,'%d/%m/%Y')
        