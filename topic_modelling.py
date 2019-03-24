import pandas as pd

data = pd.read_csv('data.csv', error_bad_lines=False);
data_text = data[['Description']]
data_text['index'] = data_text.index
documents = data_text

documents['Description'].tolist()


import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
np.random.seed(2018)

import nltk

en_stop = set(nltk.corpus.stopwords.words('english'))

import nltk
from nltk.corpus import wordnet

lmtzr = nltk.WordNetLemmatizer().lemmatize

## We lookup whether a word is and adjective, verb, noun or adverb here.
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

## This version uses word type. Needs the bigger nltp download ("popular")
def normalize_text(text):
    word_pos = nltk.pos_tag(nltk.word_tokenize(text))
    lemm_words = [lmtzr(sw[0], get_wordnet_pos(sw[1])) for sw in word_pos]

    return [x.lower() for x in lemm_words]

## This version doesn't require the "popular" download
def preprocess(text):
    lemmatizer = nltk.WordNetLemmatizer()
    return([lemmatizer.lemmatize(i) for i in text.split()])

################
## wordnet version
from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

## lemmatize
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

## This version is for comparison
def prepare_text_for_lda(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens
  
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()

def LDA(docs_raw,n_topics):
    tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                    stop_words = en_stop,
                                    # token choose the words with more than 4 length and get rid of the speical words
                                    token_pattern = r'\b\w+\b')
    dtm_tf = tf_vectorizer.fit_transform(docs_raw)
    tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
    dtm_tfidf = tfidf_vectorizer.fit_transform(docs_raw)
    # for TF DTM
    lda_tf = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    %time lda_tf.fit(dtm_tf)
    # for TFIDF DTM
    lda_tfidf = LatentDirichletAllocation(n_components=n_topics, random_state=0)
    %time lda_tfidf.fit(dtm_tfidf)
    return(lda_tf, dtm_tf, tf_vectorizer)
  

lda_tf_pwplus, dtm_tf_pwplus, tf_vectorizer_pwplus = LDA(documents['Description'].tolist(),10)
pyLDAvis.sklearn.prepare(lda_tf_pwplus, dtm_tf_pwplus, tf_vectorizer_pwplus)
