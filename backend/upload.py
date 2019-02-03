from flask_restful import Resource, reqparse
from flask import request, send_from_directory, make_response
import werkzeug
from datetime import datetime
import random as rd
from hashlib import md5
#from request_file import define_file, save_path_file
import codecs
import os

from db import Database


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
        modules = "Grupo1 Grupo2 Grupo3 Grupo4 Grupo5 Grupo6 Grupo7 Grupo8 Grupo9 Grupo10 Grupo11 Grupo12".split()
        data = request.get_json(force=True)
        db = Database('users')
        user = db.find_one({'_id': ObjectId(data['_id'])})
        if data['update_module']:
            # insert em videos_ileel com o data['path_file'] #OK
            # update em users.dataset #OK
            files = Database('videos_ileel')
            files.insert_one({
                'path_file':data['path_file'],
                'post_date': str(datetime.now()),
                'module': user['dataset']['current_module'],
                '_id_author': data['_id']
            })
            update = user
            update['dataset'] = {
                '#video': user['dataset']['#video'] +1,
                'current_module': user['dataset']['current_module']
            }
            user.update_one(update,user)
        # verifica a contagem dos videos    
        # atualiza a contagem e modulo(se necessario) 
        if user['dataset']['#video'] == self.check_capacity(user['dataset']):
            if user['dataset']['#video'] != modules[-1]:
                _module = modules[modules.index(user['dataset']['current_module']) +1]

                # busca a url do video 
                url = self.find_file(_module,user['dataset']['#video'])
                # envia o video pro front 
                response = send_from_directory(url['diretory'],url['file_name'])
                # editar headers 
                return response
            else:
                return {'status':'finally'}
        else:
            _module = modules[modules.index(user['dataset']['current_module'])+1]
            url = self.find_file(_module, user['dataset']['#video'])
            response = send_from_directory(url['diretory'],url['file_name'])
            return response

    def find_file(self,module, file_index):
        files = os.listdir('/home/victor/Grupos/' + module)
        return {
            'diretory':'/home/victor/Grupos/'+module,
            'file_name': files[file_index]
        }

    def check_capacity(dataset):
        return len(os.listdir('/home/victor/Grupos/' + dataset['current_module']))



#response = send_from_directory('./', 'pp.jpeg')
#response.headers['my-custom-header'] = 'Este sou eu Guilherme Alves'
#return response