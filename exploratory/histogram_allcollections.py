###PURPOSE: computes the number of documents for all collections in phoenix database
##currently I'm working on putting this script to work, but i don't know why, there are some problems sometimes...


import pymongo
import pdb
import os
import matplotlib.pyplot as plt
import numpy as np
from function import get_allkeys, count_occurences_field

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix
all_collections = db.collection_names()


##loop over all collections
for c in all_collections:
    print "Entering collection = ", c
    os.mkdir("figures/histograms/"+c)
    current_collection = db[c]
    document_example = current_collection.find_one()
    list_keys = get_allkeys(document_example) #get a random example (might not contain all the keys accross all documents of the current collection)
    total_number_of_documents = 
    
    for k in list_keys:
        try:
            counts_distinct = len(current_collection.distinct(k))
        except pymongo.errors.OperationFailure:
            print "operationfailure"

            
        threshold = 1000 #do not run a histogram if there are more than 100 different values for this key

        if counts_distinct <= threshold:
            data = count_occurences_field(current_collection,k)
            x = data.keys()
            y = data.values()
            pos = np.arange(len(x))+0.5

            if len(x) >1:
                if not isinstance(x[0],float):
                    x=[str(i) for i in data.keys()]

                plt.figure()
                plt.barh(pos, y)
                plt.axvline(total_number_of_documents,linestyle="dashed",color="black")
                plt.xlabel("Counts")
                plt.ylabel(k)
                plt.yticks(pos,x)
                plt.savefig("figures/histograms/"+c+"/"+k+".pdf")
                print "figure is done for =",k


            
    


