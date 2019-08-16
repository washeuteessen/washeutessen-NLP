import logging
import pymongo

class Recipes(object):
    """Class to load recipes from mongodb to a dataframe.
    """

    def __init__(self):
        """Setup connection to mongo client, database and collection.
        """
        # connect to mongo client
        self.conn = pymongo.MongoClient("192.168.99.100", 27017)

        # load database
        self.db = self.conn["recipes"]

        # load collections
        self.collection_recipes = self.db["recipes"]

        logging.info("Initialized Recipes class")

    def load(self):
        """Load recipes from mongodb to list.
        
        Returns
        -------
        list of dicts
            Containing two key value pairs each
            - _id : bson.objectid.ObjectId
            - text : str
        """
        recipes = self.collection_recipes.find(projection=["text"], limit=10000)
        recipes = [recipe for recipe in recipes]

        return recipes