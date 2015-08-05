import numpy as np
import pymongo




def count_occurences_field(collection, field):
    """Return a dictionary of keys and associated counts

    Parameters:
    ----------
    collection: MongoDB.collection
        collection to look into

    field: string
        name of field to look at. eg: "topic.type"

    Return:
    ------
    results: dictionary
        {value: counts}
        
    """ 

    list_values = collection.distinct(field) #get name of all existing value for field
    number_of_occurences = [collection.find({field:v}).count() for v in list_values]
    return dict(zip(list_values, number_of_occurences)) #reshape as dictionary
    


def get_allkeys(document):
    """Return the list of all keys (and subkeys down to 1 sublevel) of a collection

    http://stackoverflow.com/questions/9805451/how-to-find-names-of-all-collections-using-pymongo
    """


    keylist = []
    item = document
    for key in item.keys():
        if key not in keylist:
            keylist.append(key)
        if isinstance(item[key], dict):
            for subkey in item[key]:
                subkey_annotated = key + "." + subkey
                if subkey_annotated not in keylist:
                    keylist.append(subkey_annotated)
                    
        if isinstance(item[key], list):
            for l in item[key]:
                if isinstance(l, dict):
                    for lkey in l.keys():
                        lkey_annotated = key + "." + lkey + ""
                        if lkey_annotated not in keylist:
                            keylist.append(lkey_annotated)
    return sorted(keylist)
