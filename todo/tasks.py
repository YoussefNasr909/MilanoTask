from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from todo import db
from todo.models import Task
from todo.forms import TaskForm

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@tasks_bp.route('/dashboard')
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template('tasks/dashboard.html', title='Dashboard', tasks=tasks)

def get_dashboard():
    """Helper function to redirect to dashboard from index route"""
    return redirect(url_for('tasks.dashboard'))

@tasks_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.dashboard'))
    
    return render_template('tasks/add.html', title='Add Task', form=form, legend='New Task')

@tasks_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    
   
    if task.user_id != current_user.id:
        abort(403)
    
    form = TaskForm()
    
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.dashboard'))
    elif request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
    
    return render_template('tasks/edit.html', title='Edit Task', form=form, legend='Edit Task')

@tasks_bp.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    
    if task.user_id != current_user.id:
        abort(403)
    
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.dashboard'))

@tasks_bp.route('/toggle/<int:task_id>')
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    
    if task.user_id != current_user.id:
        abort(403)
    
    task.completed = not task.completed
    db.session.commit()
    
    status = "completed" if task.completed else "marked as incomplete"
    flash(f'Task {status} successfully!', 'success')
    return redirect(url_for('tasks.dashboard'))