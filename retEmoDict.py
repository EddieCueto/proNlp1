
def emoDic():

    emoDict = open('SEL.txt', 'r', encoding='utf-8')
    temp = emoDict.read()

    emoDict = temp.split('\n')

    temp = []

    for i in emoDict:
        temp.append(i.split('\t'))

    n = len(temp) -1

    del temp[n]

    for i in temp:
        del i[1]

    emoDict = {i[0]: i[1] for i in temp}

    emoDict['PRI'] = 'Positivo'
    emoDict['INE'] = 'Neutro'
    emoDict['electoral'] = 'Neutro'
    emoDict['Electoral'] = 'Neutro'
    emoDict['PAN'] = 'Negativo'
    emoDict['partido'] = 'Neutro'
    emoDict['Partido'] = 'Neutro'
    emoDict['PRD'] = 'Negativo'
    emoDict['PT'] = 'Negativo'
    emoDict['PANAL'] = 'Negativo'
    emoDict['PVEM'] = 'Negativo'
    emoDict['Movimiento'] = 'Negativo'
    emoDict['Ciudadano'] = 'Negativo'
    emoDict['Alianza'] = 'Negativo'
    emoDict['Morena'] = 'Negtivo'
    emoDict['electoral'] = 'Neutro'
    emoDict['Electoral'] = 'Neutro'
    emoDict['Encuentro'] = 'Negativo'
    emoDict['Social'] = 'Negativo'
    emoDict['Peña'] = 'Positivo'
    emoDict['Nieto'] = 'Sorpresa' #['Sorpresa', 'Positivo']

    return emoDict
