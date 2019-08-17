import logging
from gensim.summarization import keywords

from helper import Recipes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# load recipes
logging.info("Loading recipes from mongodb")
recipes = Recipes()
recipes = recipes.load()
recipes_text = [recipe["text"] for recipe in recipes]

# get keywords
logging.info("Extracting keywords.")
keywords = keywords(text=" ".join(recipes_text), words=10, scores=True)
print(keywords)