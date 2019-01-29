from flask_restful import Resource, reqparse
from flask import request, jsonify
import werkzeug
from datetime import datetime
import random as rd
from hashlib import md5


class Upload(Resource):

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
        parse.add_argument('info', type=dict, location='json')  #TODO
        args = parse.parse_args()
        audioFile = args['file']
        file_name = md5((str(datetime.now()) + str(rd.random())).encode()).hexdigest()
        path_file = 'dataset/{}.jpg'.format(file_name)
        audioFile.save(path_file)
        

        return {
            'status': 'sucess',
            'path_file': path_file
        }

    def get(self):
        
        data = request.get_json(force=True)
