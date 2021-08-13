import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
import nltk


class TextNormalizer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()

        for i in range(len(X_copy)):
            X_copy[i] = X_copy[i].lower()
            X_copy[i] = X_copy[i].replace('\n', ' ')
            X_copy[i] = X_copy[i].replace('\r', ' ')
            X_copy[i] = X_copy[i].strip()
        return X_copy


class WordExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, language, tokenize):
        self.language = language
        self.stopwords = stopwords.words(self.language)
        self.tokenize = tokenize

    def fit(self, X, y=None):
        general_freq = FreqDist()
        for txt in X:
            freq_dist = FreqDist(self.tokenize(txt))
            general_freq.update(freq_dist)
        self.hapaxes = general_freq.hapaxes()
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for i in range(len(X_copy)):
            X_copy[i] = ' '.join([token for token in self.tokenize(X_copy[i])
                                  if token not in self.stopwords and
                                  token not in self.hapaxes])
        return X_copy


class ApplyStemmer(BaseEstimator, TransformerMixin):
    def __init__(self, stemmer, tokenize):
        self.stemmer = stemmer
        self.tokenize = tokenize

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for i in range(len(X_copy)):
            X_copy[i] = ' '.join([self.stemmer.stem(token)
                                  for token in self.tokenize(X_copy[i])])
        return X_copy

