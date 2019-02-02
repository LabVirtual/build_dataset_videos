from db import Database
from datetime import datetime
from bson import ObjectId


def define_file(data):
    user_db = Database('users')
    user = user.find_one({'_id': ObjectId(data['_id'])})
    current_module = user['current_module']
    
    i = 0
    while user['dataset'][i]['module'] != current_module:
        i += 1
    if user['dataset'][i]['#video'] < 50:
        return current_module
    else:
        for x in user['dataset']
            
 

def save_path_file(data):
   pass