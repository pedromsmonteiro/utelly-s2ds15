import matplotlib.pyplot as plt
import numpy as np
import pymongo
from function import count_occurences_field

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix

##collections
genre = db.genre
event = db.event


##make the histogram
fieldname = "metadata.duration"
data = count_occurences_field(event,fieldname)
x = data.keys()
y = data.values()
X = np.arange(len(data))

ymax = max(y)*1.2

plt.figure()
plt.barh(x, y)
plt.xlabel("Counts")
plt.ylabel("Duration [minutes]")
plt.savefig("figures/histogram_duration.pdf")

