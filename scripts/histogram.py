import pymongo
import numpy as np
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost", 27017) #client to local server
db = client.phoenix #create a database when call first time

# this genre list is generated from the genre collection
genre = db.genre
genrelistfromgenre = []

for g in genre.find():
    try:
        temp = g["name"]
        genrelistfromgenre.append(temp)
    except:
        print "test"

# this genre list is generated from unique elements in the event genre entry
genrelist = db.event.distinct("topic.genres.name")

#work out the differece in the two lists
differenceinlists = list(set(genrelistfromgenre) - set(genrelist))
        
od = db.o_d_event
numberofgenre = len(genrelist)

i = 0
bin = [0 for x in range(numberofgenre)]

for n in genrelist:
    bin[i] = db.event.find({"topic.genres.name":n}).count()
    print genrelist[i], bin[i]
    i = i+1

print sum(bin)

# this plots the frequency vs genres
plt.plot(bin)
plt.xlabel('genres')
plt.ylabel('frequency')

#histogram with number of occurence
plt.hist(bin,bins=100)

#now cutoff the genres with entries less than 1000

bin = np.array(bin)

bincutoff = bin[bin > 1000]
genrecutoff = genrelist[bin > 1000]

plt.plot(bincutoff)
plt.xlabel('genres')
plt.ylabel('frequency')