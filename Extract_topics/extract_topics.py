import sys
import logging
import spacy
import gensim
from gensim import corpora
from gensim.test.utils import common_corpus, common_dictionary
from gensim.models import HdpModel, LdaModel
from helper import Recipes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# load recipes
logging.info("Loading recipes from mongodb")
recipes = Recipes()
recipes = recipes.load()
recipes_text = [recipe["text"] for recipe in recipes]

# get lemma for each word
logging.info("Cleaning recipe texts with spaCy and returning lemma.")
nlp = spacy.load("de_core_news_md")

texts = []
for document in recipes_text:
    text = []
    doc = nlp(document)
    for w in doc:
        if not w.is_stop and not w.is_punct and not w.like_num:
            text.append(w.lemma_)
    texts.append(text)

# create dictionary and corpus
logging.info("Create gensim dictionary and corpus.")
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
#tfidf = models.TfidfModel(corpus)

#
logging.info("Fit lda model on recipes data.")
model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)
print(model.show_topics())