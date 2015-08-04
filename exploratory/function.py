import numpy as np



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
        

    """ 

    ##get name of all existing value for field
    list_values = collection.distinct(field)

    ##count number of occurences of each value that field can take
    number_of_occurences = []
    for v in list_values:
        number_of_occurences.append(collection.find( { field: v} ).count())

    return list_values, number_of_occurences
    
