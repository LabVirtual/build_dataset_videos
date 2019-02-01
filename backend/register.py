from flask_restful import Resource
from flask import jsonify, request

from db import Database


class Register(Resource):

    def post(self):

        data = request.get_json(force=True)
        usr = Database('users')
        
        match = {'cpf':data['cpf']}
        if usr.find_one(match) == None:
            data['dataset'] = {
                'current_module': 'a',
                '#video': 0
            }
            usr.insert_one(data)
            return {'status': 'cadastrado'}
        else:
            return {'status': 'Já possui cadastro'}

