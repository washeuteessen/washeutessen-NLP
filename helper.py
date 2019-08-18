import logging
import pymongo

class Recipes(object):
    """Class to load recipes from mongodb to a dataframe.
    """

    def __init__(self, limit=100):
        """Setup connection to mongo client, database and collection.
        """
        # connect to mongo client
        self.conn = pymongo.MongoClient("192.168.99.100", 27017)

        # load database
        self.db = self.conn["recipes"]

        # load collections
        self.collection_recipes = self.db["recipes"]

        # define amount of items to load
        self.limit = limit

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
        logging.info(f"Load {self.limit} recipes from mongodb.")

        recipes = self.collection_recipes.find(projection=["text", "title"], limit=self.limit)

        recipes = [recipe.get("title") for recipe in recipes]
        
        recipes = [recipe for recipe in recipes if recipe is not None]

        logging.info(f"Found {len(recipes)} recipes with existing title.")

        return recipes