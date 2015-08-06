import pymongo
import numpy as np
import matplotlib.pyplot as plt
#import csv

client = pymongo.MongoClient("localhost", 27017) #client to local server
db = client.phoenix #create a database when call first time

useractivity = db.user_log.distinct("action")
numact = len(useractivity)

bincount = [0 for x in range(numact)]
i = 0

for n in useractivity:
    bincount[i] = db.user_log.find({"action":n}).count()
    print useractivity[i], bincount[i]
    i = i+1

# plot the histogram
fig,ax = plt.subplots()
width = 1.0
ind = np.arange(len(bincount))
plt.bar(ind,bincount)
plt.ylabel('times')
fig.suptitle('User log by Type')
ax.set_xticks(ind+width/2)
ax.set_xticklabels(useractivity, rotation=90)
plt.savefig("userlog.pdf")

#output to csv file
f = open("userlog.csv", "w")

for i in xrange(len(bincount)):
    f.write("{},{}\n".format(useractivity[i],bincount[i]))

f.close()

