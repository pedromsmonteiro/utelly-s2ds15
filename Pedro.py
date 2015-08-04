import pymongo
import matplotlib.pyplot as plt
import numpy as np


client = pymongo.MongoClient('localhost', 27017)
db = client.phoenix
genre = db.genre

# Print max(event.distinct("metadata.duration"))

# Print db.event.find_one()

myFile = open('genre_count.txt', 'w+')

# Defining the dictionaries and lists
counter = 0
dictionary = {}
genre_name = []
count_value = []
for a in genre.find():
# The for loop was returning a KeyError. To avoid this: I ignore the error by using the 
# Try and except conditions.
  try:
# Getting the name of the genre
    genre_name_temp = a['name']
  except KeyError:
    continue
# Counting the events for each genre in the topic => genres tree
  genre_count_temp = db.event.find({u'topic.genres.name':  genre_name_temp}).count()
# Print just if the count is bigger than 0
  if genre_count_temp != 0:
    counter += genre_count_temp
    dictionary[' genre_name_temp'] = genre_count_temp
    genre_name.append( genre_name_temp)
    count_value.append(genre_count_temp)
    print  genre_name_temp, genre_count_temp

# Staking the two lists using numpy
DAT =  np.column_stack((genre_name, count_value))
# Saving the DAT file in a .txt document using space as a delimiter and also importing 
#the values as strings(fmt='%s').


np.savetxt('genre_count.txt', DAT,delimiter=" ", fmt='%s') 

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

fieldname = "metadata.duration"
data = count_occurences_field(event,fieldname)
x = data.keys()
y = data.values()
X = np.arange(len(data))

ymax = max(y)*1.2

plt.figure()
plt.bar(X, y, align="center",width=0.5)
plt.xticks(X, x)
plt.ylim([0,ymax])
plt.show()
 
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

