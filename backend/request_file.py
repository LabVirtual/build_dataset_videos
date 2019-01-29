from db import Database
from datetime import datetime
from bson import ObjectId


def save_path_file(data):

    _conn = Database('videos_ileel')
    _conn.insert_one({
        'path_file': data['path_file'],
        'post_date': str(datetime.now()),
        '_id_author': data['_id_author']
    })

    _conn = Database('users')
    doc = _conn.find_one({'_id': ObjectId(data['_id_author'])})
    i=0
    while doc['dataset'][i] != 
    _conn.update()

def define_file(data):

    _conn = Database('users')
    doc = _conn.find_one({'_id': ObjectId(data['_id_author'])})
    # Update contagem do video
    if data['update_module']:
        array = doc['dataset']
        index = array.index(data['update_module'])
        new_doc['dataset'][index]['#video'] = doc['dataset'][index]['#video'] +1
        _conn.update_one(new_doc,doc)
        print('Contagem atualizada!')
    else:
        pass
        #TODO