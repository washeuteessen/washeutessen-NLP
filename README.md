Use NLP to enhance data quality of ingredients and prepare filter methods
|What?|Techniques|Packages|
|-----------|-----------|--|
| match different forms of an ingredients (e.g. egg --> eggs, organic egg) | Lemmatization, compute similarity by word embeddings, compute string distance (e.g. Levensthein), order alphabetically | spaCy, flair |
|extract topics from recipes as basis for filter|Topic Modelling/Extraction|gensim|
| extract keywords from recipes as basis for filter | keyword extraction, NER, stopwords removal |spaCy |
| Develop dictionary of neutral ingredients, dairy and meat/fish as basis for vegetarian/vegan filter|rule based matching|-|