import yaml

rawDat = open('rss_univ.txt', 'r')

strDat = rawDat.read()

rawDat = strDat.split(';\n')

# rawDat = yaml.load(rawDat[0])

print(rawDat[0])
