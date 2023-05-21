from models.db import db

class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(75), unique=True)
    senha = db.Column(db.String(12))
    birth_date  = db.Column(db.DateTime)

    clients = db.relationship('Client', backref='person')
    employees = db.relationship('Employee', backref='person')
