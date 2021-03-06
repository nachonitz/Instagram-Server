from flask import request, jsonify
from flask_restful import Resource
import app.Instagram.main

class VideoRoute(Resource):
    @staticmethod
    def get(persona=None):
        username_id = request.headers.get('username_id')
        token = request.headers.get('token')
        rank_token = request.headers.get('rank_token')
        uuid = request.headers.get('uuid')
        sessionid = request.headers.get('sessionid')
        print(sessionid)
        profile = app.Instagram.main.get_profile(persona, username_id, token, rank_token, uuid, sessionid)
        response = jsonify(profile)
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
