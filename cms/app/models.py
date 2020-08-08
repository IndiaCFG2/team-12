from datetime import datetime
from app import db

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Admin {}>'.format(self.username)    

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_num = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    class_id = db.Column(db.Integer, db.ForeignKey('class.id')) #

    def __repr__(self):
        return '<Student {}>'.format(self.username)    

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))    
    class_id = db.Column(db.Integer, db.ForeignKey('class.id')) #
    session = db.relationship('Session', backref='teacher', lazy=True)

    def __repr__(self):
        return '<Teacher {}>'.format(self.username)    

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)    
    session = db.relationship('Session', backref='course', lazy=True)
    resouce = db.relationship('Resource', backref='course', lazy=True)

    def __repr__(self):
        return '<Course {}>'.format(self.username)    

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    chapter = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64), index=True, unique=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id')) #

    def __repr__(self):
        return '<Resource {}>'.format(self.name)    


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)    
    school = db.relationship('School', backref='board', lazy=True)

    def __repr__(self):
        return '<Board {}>'.format(self.name)  

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id')) #
    class_ = db.relationship('Class', backref='school', lazy=True)

    def __repr__(self):
        return '<School {}>'.format(self.name)   

class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id')) #
    student = db.relationship('Student', backref='class', lazy=True)
    teacher = db.relationship('Teacher', backref='class', lazy=True)

    def __repr__(self):
        return '<Class {}>'.format(self.username)   

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    start_time = db.Column(db.DateTime(), index=True)
    end_time = db.Column(db.DateTime(), index=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id')) #
    course_id = db.Column(db.Integer, db.ForeignKey('course.id')) #

    def __repr__(self):
        return '<Session {}>'.format(self.username)           