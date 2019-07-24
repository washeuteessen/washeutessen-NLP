import spacy
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin, BaseEstimator

pipeline_match = Pipeline([
    ("Lemmatizer", SpacyLemmatizer()),
    #("WordEmbedder", WordEmbedder())
])

class SpacyLemmatizer(BaseEstimator, TransformerMixin):
    """Class to call spacy nlp pipeline and extract lemma for each word
    
    Parameters
    ----------
    BaseEstimator : sklearn base class
    TransformerMixin : sklearn base class       
    """
    def __init__(self):
        self.nlp = spacy.load("de_core_news_md")

    def fit(self, X, y=None):
        pass

    def transform(self, X):
        """Function to retrieve lemma for each word. 
        
        Parameters
        ----------
        X : df
            Dataframe with word in first column
        
        Returns
        -------
        dict
            Dataframe with word in first column and corresponding lemma in second column.
        """
        # iterate over dataframe
        for idx, row in X.iterrows():

            # apply spacy nlp pipeline on word
            doc = self.nlp(row[0])

            # retrieve lemma for each token
            for token in doc:
                lemma = token.lemma_

            # write lemma to df
            X.iloc[idx,1] = lemma

        return X