from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    from app import models
    
    migrate.init_app(app, db)
    bootstrap.init_app(app)

    from app.medicos import bp_medicos
    from app.pacientes import bp_pacientes
    from app.citas import bp_citas

    app.register_blueprint(bp_medicos, url_prefix='/medicos')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')

    return app