from flask import request, jsonify
from flask_restful import Resource
import app.Instagram.main

class LoginRoute(Resource):
    @staticmethod
    def get(persona=None):
        profile = app.Instagram.main.get_profile(persona)
        response = jsonify(profile)
        response.status_code = 200
        return response
    @staticmethod
    def post():
        print(request.headers)
        username = request.headers.get('username')
        password = request.headers.get('password')
        print("AAA")
        print(username)
        portable_data = app.Instagram.main.login(username, password)
        response = jsonify(portable_data)
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
