###PURPOSE: print the number of events which have a N number of events

import pymongo

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix

genre = db.genre
event = db.event

maxn=10 #max number of genres we are looking for
for n in range(0,maxn):
    print event.find({ "topic.genres": { "$size": n } } ).count()




    
