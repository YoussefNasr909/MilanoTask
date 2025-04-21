from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()

def create_app(test_config=None):
    
    app = Flask(__name__, instance_relative_config=True)
    
    
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-key-for-testing'),
        SQLALCHEMY_DATABASE_URI='sqlite:///todo.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        
        app.config.from_pyfile('config.py', silent=True)
    else:
        
        app.config.from_mapping(test_config)

   
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    db.init_app(app)
    
   
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
   
    from todo.models import User, Task
    
    
    from todo.auth import auth_bp
    from todo.tasks import tasks_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    with app.app_context():
        db.create_all()
    
   
    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'now': datetime.utcnow()}
    
    @app.route('/')
    def index():
        from flask import render_template
        from flask_login import current_user
        if current_user.is_authenticated:
            return tasks_bp.get_dashboard()
        return render_template('index.html')
    
    return app