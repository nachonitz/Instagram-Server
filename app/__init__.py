# pylint: skip-file

from flask import Flask
import flask_sqlalchemy
from flask_restful import Api
from flask_migrate import Migrate
from config import Config

import firebase_admin
from firebase_admin import credentials


cred = credentials\
    .Certificate("chotuve-467b2-firebase-adminsdk-zuv00-1dbee4cba5.json")
firebase_admin.initialize_app(cred)

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
    from .image_routes import ImageRoute

    app_api.add_resource(VideoRoute, '/videos', '/videos/<int:id_video>')
    app_api.add_resource(ImageRoute, '/images', '/images/<int:id_image>')


app = create_app()
api = Api(app)
add_routes(api)
