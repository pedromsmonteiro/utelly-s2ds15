###PURPOSE: computes the number of documents for all collections in phoenix database

import pymongo

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix
all_collections = db.collection_names()


##loop over all collections
for c in all_collections:
    print c, db[c].find().count()

genre = db.genre
event = db.event
