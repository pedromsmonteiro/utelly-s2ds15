# this scripts identifies the heavy users
import pymongo
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost", 27017) #client to local server
db = client.phoenix #create a database when call first time

uidlist = db.user_activity.distinct("user_id")
bin = [0 for x in range(len(uidlist))]

i=0

for u in uidlist:
    bin[i] = db.user_activity.find({"user_id":u}).count()
    print uidlist[i], bin[i]
    i = i+1

fig = plt.figure()    
plt.bar(range(100),bin[0:100:1])
plt.savefig("userstats.pdf")

fig = plt.figure()    
plt.bar(range(len(bin)),bin)
plt.savefig("userstats.pdf")
