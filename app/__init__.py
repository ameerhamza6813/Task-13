from flask import Flask
from .db import db
from .routes import main
from .scheduler import init_scheduler

def create_app():
    from config import Config
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(main)

    init_scheduler(app)

    return app
