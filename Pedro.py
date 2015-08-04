import pymongo
import matplotlib.pyplot as plt
import numpy as np


client = pymongo.MongoClient('localhost', 27017)
db = client.phoenix
genre = db.genre

#print max(event.distinct("metadata.duration"))

#print db.event.find_one()

myFile = open('genre_count.txt', 'w+')


counter = 0
dictionary = {}
qq = []
for a in genre.find():
  try:
    aa = a['name']
  except KeyError:
    print 'No Name'
  bb = db.event.find({u'topic.genres.name': aa}).count()
  if bb != 0:
    counter += bb
    dictionary['aa'] = bb
    cc = str(aa)+ " " +str(bb)
    qq.append(cc)
    print aa, bb


np.savetxt('genre_count.txt', cc, fmt='%1.4e') 

# names = dictionary.keys()
# 
# ax = plt.subplot(111)
# width=0.3
# bins = map(lambda x: x-width/2,range(1,len(dictionary)+1))
# ax.bar(bins,data,width=width)
# ax.set_xticks(map(lambda x: x, range(1,len(dictionary)+1)))
# ax.set_xticklabels(names,rotation=45)
# 
# plt.show()


 
print "total", counter  
    
# 
# 
# 
# 
# import pymongo
# 
# client = pymongo.MongoClient('localhost', 27017)
# 
# db = client.phoenix
# collection = db.phoenix


# for a in genre.find():
#   z = a[u'name']
#   for b in genre.find():
#     y = b[u'name']
#     if z in y:
#       print db.genre.find_one({"name" : "b"})
#       print db.genre.find({"name" : "b"}).count()

