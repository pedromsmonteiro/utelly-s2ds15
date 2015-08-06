import pymongo

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix
collections = db.collection_names()

