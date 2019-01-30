from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['dataset_ileel']

collection = db['users']
exemplo_1 = {
    "name": "Guilherme",
    "last_name": "Alves",
    "cpf": "018.581.296-13",
    "password": "ileel",
    "email": "guilherme.alves3340@gmail.com",
    "sex": "M",
    "nationality": "brasileiro",
    "city": "uberlandia",
    "state": "mg",
    "date_birth": "27-01-1997",
    "registration_date": "24-01-2019",
    "dataset": {
        "module_current": "a",
        "#video": 25
    }
}
collection.insert_one(exemplo_1)


collection = db['videos_ileel']
exemplo_2 = {
    "post_date": "12-01-2019",
    "path_file": "/home/ileel/dataset/asd6a4sdasd.mp4",
    "_id_author": "adfsdfsdfsfs654sdf64sfsf",
    "module": "a"
}
