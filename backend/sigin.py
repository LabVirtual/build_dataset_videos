from flask_restful import Resource
from flask import request, jsonify
from bson import ObjectId
from hashlib import md5

from db import Database


class Sigin(Resource):

    def get(self):
        data = request.get_json(force=True)
        usr = Database('users')
        result = usr.find_one({'cpf':data['cpf']})
        if result != None:
            if result['password'] == md5(data['password']).hexdigest():
                return {
                    'status': 'ok',
                    'name': result['name'],
                    'last_name': result['last_name'],
                    '_id': str(result['_id']),
                    'current_module': result['current_module']
                }
            else:
                return {'status': 'error'}

        else:
            return {'status': 'error'}