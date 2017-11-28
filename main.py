
from retEmoDict import emoDic
from newsTrain import classifyNews
from clust import clustering


temp = clustering()

emoDict = emoDic()

rest = []

for i in temp:
    rest.append(classifyNews(i, emoDict))


for i in rest:
    print(i)

