import pymongo
import numpy as np
import matplotlib.pyplot as plt
import csv

client = pymongo.MongoClient("localhost", 27017) #client to local server
db = client.phoenix #create a database when call first time

#db.user_activity.find()

useractivity = db.user_activity.distinct("type")
numact = len(useractivity)

bincount = [0 for x in range(numact)]
i = 0

for n in useractivity:
    bincount[i] = db.user_activity.find({"type":n}).count()
    print useractivity[i], bincount[i]
    i = i+1

fig,ax = plt.subplots()
width = 1.0
ind = np.arange(len(bincount))
plt.bar(ind,bincount)
plt.ylabel('times')
fig.suptitle('User Activities by Type')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(useractivity, rotation=90)
plt.savefig("useractivity.pdf")

f = open("useractivity.csv", "w")

for i in xrange(len(bincount)):
    f.write("{},{}\n".format(useractivity[i],bincount[i]))

f.close()

#fig.autofmt_xdate()

#print db.user_log.distinct("action")
#print db.user_activity.distinct("date")
#print db.user.distinct("name")

#UserName = db.user.distinct("name")

#ActionPlay = db.user_activity.find({"type":u'PLAY'})

#ActionPlay = db.user_activity.find({"date":"2014"})

#for i in ActionPlay:
#    print i
    
