###PURPOSE: computes the number of documents for all collections in phoenix database
##currently I'm working on putting this script to work, but i don't know why, there are some problems sometimes...


import pymongo
import pdb
import os
import matplotlib.pyplot as plt
import numpy as np
from function import get_allkeys, count_occurences_field, type_to_string

client = pymongo.MongoClient("localhost", 27017) 
db = client.phoenix
all_collections = db.collection_names()
#all_collections= [u'page',u'refining_list',u'reminder',u'saved_search',u'search_result',u'status',u'topic',u'topic_type',u'user',u'user_activity',u'user_log',u'user_topic']

threshold = 200 #do not run a histogram if there are more than N different values for this key

##define output
root_output = "figures/histograms/"
if not os.path.isdir(root_output):
    os.mkdir(root_output)



### MAIN LOOP
for c in all_collections:

    ##create directory for output
    print "Entering collection = ", c
    if not os.path.isdir(root_output+c):
        os.mkdir(root_output+c)

    ##get keys
    current_collection = db[c]
    document_example = current_collection.find_one()
    list_keys = get_allkeys(document_example) #get a random example (might not contain all the keys accross all documents of the current collection)
    total_number_of_documents = current_collection.find().count()
    
    for k in list_keys:
        try:
            counts_distinct = len(current_collection.distinct(k))
        except pymongo.errors.OperationFailure: #if returns too many documents
            print "operationfailure"

        if counts_distinct <= threshold:
            data = count_occurences_field(current_collection,k)
            x = data.keys()
            y = data.values()
            pos = np.arange(len(x))+0.5

            if len(x) > 1: #do not plot if only 1 element
                if not isinstance(x[0],float): #keep float for plot
                    x = [type_to_string(i) for i in data.keys()]
                    x = [i.decode('utf-8') for i in x]                    

                plt.figure()
                plt.barh(pos, y)
                plt.axvline(total_number_of_documents,linestyle="dashed",color="black")
                plt.xlabel("Counts")
                plt.ylabel(k)
                plt.yticks(pos+0.5,x)
                try:
                    plt.tight_layout()
                except ValueError: #xlabel are very long
                    print "text too long"
                    
                try:
                    plt.savefig(root_output+c+"/"+k+".pdf")
                except ValueError: #xlabel are very long
                    print "text too long"
                    
                    
                print "figure is done for =",k


            
    


