from infBack import get_vect as gv
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def stopWrdList():
    sw = open('stop.words')
    prue = []
    prue.append(sw.readlines())
    return [l.strip('\n\r') for l in prue[0]]


voc = ["ine", "pri", "pan", "prd", "pt", "pvem", "verde", "movimiento", "ciudadano", "panal", "alianza", "morena", "partido", "encuentro", "social", "electoral"]

stop_words = stopWrdList()

dataVect = gv()

dataVect = np.array(dataVect)

corpus = dataVect[:, 2]

vectorizer = TfidfVectorizer(strip_accents='ascii', analyzer='word', stop_words=stop_words, vocabulary=voc)

X = vectorizer.fit_transform(corpus)

del dataVect, stop_words, vectorizer  # , corpus

J = X.toarray()

# print(J)

index = []

for x in range(0, len(J)):
    if sum(J[x]) != 0:
        index.append(x)

index = tuple(index)

electCorp = [corpus[x] for x in index]

del corpus

print(electCorp)
