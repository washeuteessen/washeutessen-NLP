import logging
from gensim.summarization import keywords
from multi_rake import Rake

from helper import Recipes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# load recipes
logging.info("Loading recipes from mongodb")
recipes = Recipes(limit=1000)
recipes = recipes.load()
recipes_text = [recipe["text"] for recipe in recipes]

# get keywords
logging.info("Extracting keywords.")
#keywords = keywords(text=" ".join(recipes_text), words=10, scores=True, pos_filter=("NN", "NNS"))
rake = Rake(max_words=2, language_code="de")
keywords = rake.apply(" ".join(recipes_text))[:20]
print(keywords)