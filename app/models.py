from .db import db
from datetime import datetime, date

class User(db.Model):
    __tablename__ = "users"  # 👈 Explicit table name to avoid conflicts
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    habits = db.relationship('Habit', backref='user', lazy=True)


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    frequency = db.Column(db.String(20))  # daily or weekly
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    check_ins = db.relationship('CheckIn', backref='habit', lazy=True)

class CheckIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'), nullable=False)
    date = db.Column(db.Date)

class ReportLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    week_start = db.Column(db.Date)
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="sent")
