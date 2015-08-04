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
        {value: counts}
        
    """ 

    list_values = collection.distinct(field) #get name of all existing value for field
    number_of_occurences = [collection.find({field:v}).count() for v in list_values]
    return dict(zip(list_values, number_of_occurences)) #reshape as dictionary
    




    
