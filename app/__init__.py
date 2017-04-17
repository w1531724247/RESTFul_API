from flask import Flask, request
from flask_mongoengine import MongoEngine
from config import config

db = MongoEngine()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from base import base as base_blueprint
    app.register_blueprint(base_blueprint, url_prefix='/base')
    from api import test as test_blueprint
    app.register_blueprint(test_blueprint, url_prefix='/test')
    from api import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
