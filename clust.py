from infBack import get_vect as gv
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import cluster
from matplotlib import pyplot
import numpy as np

def stopWrdList():
    sw = open('stop.words')
    prue = []
    prue.append(sw.readlines())
    return [l.strip('\n\r') for l in prue[0]]


stop_words = stopWrdList()

dataVect = gv()

dataVect = np.array(dataVect)

corpus = dataVect[:, 2]

vectorizer = CountVectorizer(stop_words=stop_words)
transformer = TfidfTransformer(smooth_idf=False)

X = vectorizer.fit_transform(corpus)

del dataVect, corpus, stop_words

J = X.toarray()

tf_idf = transformer.fit_transform(J)

tf_idf_matrix = tf_idf.toarray()

k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(J)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

for i in range(k):
    # select only data observations with cluster label == i
    ds = J[np.where(labels == i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i, 0], centroids[i, 1], 'kx')
    # make the centroid x's bigger
    pyplot.setp(lines, ms=15.0)
    pyplot.setp(lines, mew=2.0)
pyplot.show()

print(X.toarray())
