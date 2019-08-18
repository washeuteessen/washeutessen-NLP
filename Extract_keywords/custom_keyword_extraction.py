import sys
import logging
from Extract_keywords.keywords_helper import Keywords
from helper import Recipes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# load recipes
logging.info("Loading recipes from mongodb")
recipes = Recipes(limit=10000)
recipes = recipes.load()
recipes_text = [recipe for recipe in recipes]

# get keywords
logging.info("Extracting keywords.")
extractor = Keywords(max_df=1, n_words=10)
keywords = extractor.extract(texts=recipes_text)
print(keywords)