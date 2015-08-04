import pymongo

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix

genre = db.genre
event = db.event
o_d_events = db.o_d_event


for g in genre.find():
    print g

# ##make a list of all genre
# list_genre=[]
# for g in genre.find():
#     try:
#         list_genre.append(g["name"])
#         i=i+1
#     except(KeyError):
#         print "no name"
