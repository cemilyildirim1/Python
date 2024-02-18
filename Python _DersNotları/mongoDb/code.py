import pymongo
from pymongo import MongoClient

Cluster = MongoClient("mongodb://localhost:27017/")
db = Cluster["local"]
collection = db["startup_log"]


deneme = {"_id":1,"_name":"Cemil","_surname":"Yıldırım"}
x = collection.insert_one(deneme)

# print(db.list_collection_names())

print(x.inserted_id)