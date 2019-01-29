from pymongo import MongoClient

from mongo_config import mongo


class Database():

    def __init__(self, collection):
        self.client = MongoClient('mongodb://{}:{}'.format(mongo['host'],mongo['port']))
        self.client = MongoClient('localhost',27017)
        self.collection = self.client[mongo['database']][collection]

    def find_one(self, json):
        query = self.collection.find_one(json)
        if query:
            return query
        else:
            None

    def insert_one(self, json):
        return self.collection.insert_one(json)

    def update(self, new_json, json):
        newvalues = { "$set": new_json }
        return self.collection.update_one(json, newvalues)


