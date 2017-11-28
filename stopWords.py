

def stopWrdList():
    sw = open('stop.words')
    prue = []
    prue.append(sw.readlines())
    return [l.strip('\n\r') for l in prue[0]]
