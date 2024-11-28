from pymongo import MongoClient

class Mongo_connection:
    def __init__(self):
        self.mongo_client = MongoClient("localhost", 27017)
        self.db = self.mongo_client['mqtt_data']
        self.collection = self.db['messages']