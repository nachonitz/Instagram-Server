# pylint: skip-file

from flask import Flask
#import flask_sqlalchemy
from flask_restful import Api
#from flask_migrate import Migrate
from flask_cors import CORS



#db = flask_sqlalchemy.SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, origins=["*"], send_wildcard=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
    #db.init_app(app)
    #Migrate(app, db)
    return app


def add_routes(app_api):
    from .video_routes import VideoRoute
    from .login_routes import LoginRoute

    app_api.add_resource(VideoRoute, '/profile', '/profile/<string:persona>')
    app_api.add_resource(LoginRoute, '/login', '/login/<string:persona>')

app = create_app()
api = Api(app)
add_routes(api)
