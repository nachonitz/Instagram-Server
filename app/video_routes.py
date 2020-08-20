from flask import request, jsonify
from flask_restful import Resource
import app.Instagram.main

class VideoRoute(Resource):
    @staticmethod
    def get(persona=None):
        lista = app.Instagram.main.get_unfollowers(persona)
        response = jsonify(lista)
        response.status_code = 200
        return response
    @staticmethod
    def post():
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
    @staticmethod
    def put(persona=None):
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
    @staticmethod
    def delete(persona=None):
        response = jsonify({"id": "hola"})
        response.status_code = 200
        return response
