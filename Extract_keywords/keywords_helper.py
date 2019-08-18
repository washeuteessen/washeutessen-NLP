import logging
import spacy
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

class Keywords(object):
    def __init__(self, max_df, n_words=10):
        # load german language model
        # TODO: dismiss unwanted spacy model parts or at nlp()
        self.nlp = spacy.load("de_core_news_md")

        # set max_df and n_words
        self.max_df = max_df
        self.n_words = n_words

    def clean(self, texts):
        """Apply spaCy's nlp pipeline on text and extract lemma fo rall NOUNs.
        
        Parameters
        ----------
        texts : list of str
            Documents texts as list to be cleaned.
        
        Returns
        -------
        list of str
            Each item contains cleaned representation of input texts.
        """
        texts_cleaned = []

        # TODO: exchange for loop with faster option, e.g. apply
        for text in texts:
            logging.info(f"Run spaCy's nlp pipeline on '{text[:30]}'")
            doc = self.nlp(text)

            #Extract lemma for each noun.
            doc_cleaned = [w.lemma_ for w in doc if w.pos_ == "NOUN"]

            texts_cleaned.append(" ".join(doc_cleaned))

        return texts_cleaned

    def count(self, texts, n_words):
        """Count word frequencies.
        
        Parameters
        ----------
        texts : str
            Containing tokens to be counted.
        
        Returns
        -------
        pd.Series
            Top n words and corresponding count.
        """
        # initialize sklearn's CountVectorizer
        vectorizer = CountVectorizer(max_df=self.max_df, ngram_range=(2,2))

        logging.info("Compute word frequencies.")
        count = vectorizer.fit_transform(texts)

        # write results to dataframe
        count = pd.DataFrame(count.todense(), columns=vectorizer.get_feature_names())

        # get number of occurences of each word over all documents
        count = count.sum(axis=0)

        # get top n words
        top_n = count.nlargest(self.n_words, keep="first")

        return top_n

    def extract(self, texts):
        
        doc = self.clean(texts)

        top_n = self.count(doc, self.n_words)

        return top_n
