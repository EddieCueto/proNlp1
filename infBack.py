import yaml
import feedparser as fp

rawDat = open('rss_univ.txt', 'r')

strDat = rawDat.read()

rawDat = strDat.split(';\n')
index = len(rawDat) - 1
rawDat.pop(index)

strDat = yaml.load(rawDat[0])

# this section of the code show how to extract relevant data from the dictionaries
print(len(rawDat))
print(strDat['entries'][0]['title'])
print(strDat['entries'][0]['links'][0]['href'])
print(strDat['entries'][0]['summary'])
