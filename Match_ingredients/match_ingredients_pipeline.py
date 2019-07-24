import spacy
from sklearn.pipeline import Pipeline
from match_ingredients_pipeline import SpacyLemmatizer

pipeline_match = Pipeline([
    ("Lemmatizer", SpacyLemmatizer()),
    #("WordEmbedder", WordEmbedder())
])