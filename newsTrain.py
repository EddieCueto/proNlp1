

def classifyNews(word_array, dict):

    default = 'NA'
    alegria = []
    enojo = []
    miedo = []
    repulsion = []
    sorpresa = []
    tristeza = []
    proper = []
    part = []

    for word in word_array:
        if dict.get(str(word), default) == 'Alegría':
            alegria.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Enojo':
            enojo.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Miedo':
            miedo.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Repulsión':
            repulsion.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Sorpresa':
            sorpresa.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Tristeza':
            tristeza.append(1)
            proper.append(word)

        if dict.get(str(word), default) == 'Positivo':
            part.append('PRI')
            proper.append(word)

        if dict.get(str(word), default) == 'Negativo':
            part.append('CONTRA')
            proper.append(word)

        if dict.get(str(word), default) == 'Neutro':
            part.append('NEU')
            proper.append(word)

        if dict.get(str(word), default) == 'NA':
            proper.append(word)


    part = set(part)
    flag = list(part)
    vect = set(proper)
    vect = list(vect)
    tot = len(word_array)

    alegria = sum(alegria)
    enojo = sum(enojo)
    miedo = sum(miedo)
    repulsion = sum(repulsion)
    sorpresa = sum(sorpresa)
    tristeza = sum(tristeza)

    pos = (alegria + sorpresa) / tot
    neg = (enojo + miedo + repulsion + tristeza) / tot

    if len(flag) == 0:
        flag = ['NEU']

    return [('Positive:', pos), ('Negative:', neg), flag, vect]


