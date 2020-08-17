from flask import request, jsonify
from flask_restful import Resource


class VideoRoute(Resource):
    @staticmethod
    def get(id_video=None):
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
    @staticmethod
    def post():
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
    @staticmethod
    def put(id_video=None):
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
    @staticmethod
    def delete(id_video=None):
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
