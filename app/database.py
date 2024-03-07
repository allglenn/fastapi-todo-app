from pymongo import MongoClient

def get_database():
    client = MongoClient("mongodb://mongodb:27017/")
    return client['todo_database']
