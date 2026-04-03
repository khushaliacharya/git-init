from datetime import datetime
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sessions = db.relationship('Session', backref='task', lazy=True, cascade="all, delete-orphan")

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
