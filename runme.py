from pymongo import MongoClient

def connect():
    connection = pymongo.MongoClient("homer.stuy.edu")
    db = connection.test
    return db.restaurants

def get_by_borough(b):
    return connect().find
