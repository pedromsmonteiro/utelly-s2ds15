import pymongo

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix
event = db.event


print max(event.distinct("metadata.duration"))
