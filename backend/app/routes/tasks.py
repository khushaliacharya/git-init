from flask import Blueprint, request, jsonify
from app import db
from app.models import Task, Session
from pydantic import ValidationError, BaseModel

bp = Blueprint('tasks', __name__)

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

@bp.route('', methods=['GET'])
def get_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return jsonify([{
        'id': t.id, 'title': t.title, 'completed': t.completed,
        'total_focus_minutes': sum(s.duration_minutes for s in t.sessions)
    } for t in tasks]), 200

@bp.route('', methods=['POST'])
def create_task():
    try:
        data = TaskCreate(**request.json)
        task = Task(title=data.title)
        db.session.add(task)
        db.session.commit()
        return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed}), 201
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    try:
        data = TaskUpdate(**request.json)
        if data.title: task.title = data.title
        if data.completed is not None: task.completed = data.completed
        db.session.commit()
        return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed}), 200
    except ValidationError:
        return jsonify({'error': 'Invalid payload'}), 400

@bp.route('/<int:task_id>/sessions', methods=['POST'])
def log_session(task_id):
    Task.query.get_or_404(task_id)
    data = request.json
    duration = int(data.get('duration_minutes', 25))
    session = Session(task_id=task_id, duration_minutes=duration)
    db.session.add(session)
    db.session.commit()
    return jsonify({'message': 'Session logged', 'id': session.id}), 201
