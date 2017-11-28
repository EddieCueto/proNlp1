from infBack import get_vect as gv
from sklearn.feature_extraction.text import TfidfVectorizer
from stopWords import stopWrdList
import numpy as np


def clustering():

    # This are the relevant news cue words
    voc = ["ine", "pri", "pan", "prd", "pt", "pvem", "verde", "movimiento", "ciudadano", "panal", "alianza", "morena", "partido", "encuentro", "social", "electoral"]

    stop_words = stopWrdList()

    dataVect = gv()

    dataVect = np.array(dataVect)

    corpus = dataVect[:, 2]

    vectorizer = TfidfVectorizer(strip_accents='ascii', analyzer='word', stop_words=stop_words, vocabulary=voc)

    X = vectorizer.fit_transform(corpus)

    del dataVect, stop_words, vectorizer  # , corpus

    J = X.toarray()

    # The indexes are extracted to obtain only the relevant news from the general corpus

    index = []

    for x in range(0, len(J)):
        if sum(J[x]) != 0:
            index.append(x)

    index = tuple(index)

    electCorp = [corpus[x] for x in index]

    del corpus

    # This section of the code processes the political party news in order to give a emotional classification

    temp = []

    for i in electCorp:
        temp.append(i.split(' '))

    return temp
