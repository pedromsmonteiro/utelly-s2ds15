def load_tweets(ifile):
    """Return the list of tweets"""

    import pickle

    f = open(ifile, 'r').read()
    f = pickle.loads(f)

    return f


def load_db(hostname="localhost",port=27017):
    """Return the mongo database"""
    
    import pymongo

    client = pymongo.MongoClient(hostname, port) 
    db = client.phoenix

    return db

