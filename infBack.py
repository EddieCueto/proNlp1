def get_vect():

    import yaml

    rawDat = open('rss_univ.txt', 'r')

    strDat = rawDat.read()

    rawDat = strDat.split(';\n')

    index = len(rawDat) - 1
    rawDat.pop(index)

    strDat = []

    for i in rawDat:
        strDat.append(yaml.load(i))

    del rawDat

    impDat = []
    for d in strDat:
        impDat.append([d['entries'][0]['title'], d['entries'][0]['links'][0]['href'], d['entries'][0]['summary']])

    del strDat

    return impDat



# this section of the code show how to extract relevant data from the dictionaries
"""
print(dic['entries'][0]['title'])
print(dic['entries'][0]['links'][0]['href'])
print(dic['entries'][0]['summary'])
"""
