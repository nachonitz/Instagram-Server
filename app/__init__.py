# pylint: skip-file

from flask import Flask
import flask_sqlalchemy
from flask_restful import Api
from flask_migrate import Migrate
from config import Config




db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    Migrate(app, db)
    return app


def add_routes(app_api):
    from .video_routes import VideoRoute

    app_api.add_resource(VideoRoute, '/videos', '/videos/<int:id_video>')

app = create_app()
api = Api(app)
add_routes(api)
