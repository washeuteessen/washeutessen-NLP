Use NLP to enhance data quality of ingredients and prepare filter methods

|| What? | Techniques | Packages |
|-|-------------------|-------:|---:|
|1| match different forms of an ingredients (e.g. egg --> eggs, organic egg) | Lemmatization, compute similarity by word embeddings, compute string distance (e.g. Levensthein), order alphabetically, coreference resolution | spaCy, flair, GermaNet Uni Tübingen, allennlp |
|2| extract topics from recipes as basis for filter|Topic Modelling/Extraction | gensim|
|3| extract keywords from recipes as basis for filter | keyword extraction (based on PageRank algorithm), NER, stopwords removal | spaCy, gensim.summarization |
|4| Develop dictionary of neutral ingredients, dairy and meat/fish as basis for vegetarian/vegan filter|rule based matching | ??? |