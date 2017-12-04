from sklearn.feature_extraction.text import TfidfVectorizer
from stopWords import stopWrdList
from retEmoDict import emoDic
from clust import clustering

def trainPre(word_array, dict):

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

    return [pos, neg, flag, vect]

def corporizer():
    emoDict = emoDic()
    clust = clustering()

    temp = []
    for i in clust:
        temp.append(trainPre(i, emoDict))

    tempy = []
    for vect in temp:
        tempy.append(' '.join(vect[3]))

    return tempy


def flagger():

    emoDict = emoDic()
    clust = clustering()

    temp = []
    for i in clust:
        temp.append(trainPre(i, emoDict))

    flag = []
    for j in temp:
        #print(j[2])
        if j[2] == (['CONTRA', 'NEU', 'PRI'] or ['NEU', 'CONTRA', 'PRI'] or ['NEU', 'PRI', 'CONTRA'] or
                        ['PRI', 'NEU', 'CONTRA'] or ['CONTRA', 'PRI', 'NEU'] or ['PRI', 'CONTRA', 'NEU']):
            flag.append(1)

        #else:
        #    flag.append(0)

        if j[2] == (['CONTRA', 'PRI'] or ['PRI', 'CONTRA']):
            flag.append(1)

        #else:
        #    flag.append(6)

        if j[2] == ['NEU']:
            flag.append(1)

        #else:
        #    flag.append(7)

        if j[2] == (['PRI'] or ['NEU', 'PRI'] or ['PRI', 'NEU']):
            flag.append(2)

        #else:
        #    flag.append(8)

        if j[2] == (['CONTRA'] or ['NEU', 'CONTRA'] or ['CONTRA', 'NEU']):
            flag.append(3)

        #else:
        #    flag.append(9)


    index = []
    for i in temp:
        if i[0] == i[1]:
            index.append(1)

        if i[0] > i[1]:
            index.append(2)

        if i[0] < i[1]:
            index.append(3)



    lenFlag = len(flag)
    lenInde = len(index)

    if lenFlag < lenInde:
        for i in range(lenInde - lenFlag):
            flag.append(1)


    return (index, flag)


def operate_on_Narray(A, B, function):
    try:
        return [operate_on_Narray(a, b, function) for a, b in zip(A, B)]
    except TypeError as e:
        # Not iterable
        return function(A, B)




def trainVect():

    flag = flagger()
    corpus = corporizer()

    stop_words = stopWrdList()

    vectorizer = TfidfVectorizer(strip_accents='ascii', analyzer='word', stop_words=stop_words, max_features=100)

    X = vectorizer.fit_transform(corpus)
    vector = X.toarray()

    long = len(flag[0])

    part_neu_ind = []
    part_neg_ind = []
    part_pos_ind = []
    cont_neu_ind = []
    cont_neg_ind = []
    cont_pos_ind = []
    neut_neu_ind = []
    neut_neg_ind = []
    neut_pos_ind = []

    # flag 0 has emotion info, flag 1 has political party info
    # 1 is neutral emo ; 2 is positive emo ; 3 is negative emo
    # 1 is neutral ; 2 is pol; 3 is opposition

    for s in range(long):
        if flag[0][s] == 1 and flag[1][s] == 1:
            neut_neu_ind.append(s)

        if flag[0][s] == 1 and flag[1][s] == 2:
            part_neu_ind.append(s)

        if flag[0][s] == 1 and flag[1][s] == 3:
            cont_neu_ind.append(s)

        if flag[0][s] == 2 and flag[1][s] == 2:
            part_pos_ind.append(s)

        if flag[0][s] == 2 and flag[1][s] == 3:
            cont_pos_ind.append(s)

        if flag[0][s] == 2 and flag[1][s] == 1:
            neut_pos_ind.append(s)

        if flag[0][s] == 3 and flag[1][s] == 1:
            neut_neg_ind.append(s)

        if flag[0][s] == 3 and flag[1][s] == 2:
            part_neg_ind.append(s)

        if flag[0][s] == 3 and flag[1][s] == 3:
            cont_neg_ind.append(s)

        part_neu_vect = [vector[x] for x in part_neu_ind]
        part_neg_vect = [vector[x] for x in part_neg_ind]
        part_pos_vect = [vector[x] for x in part_pos_ind]
        cont_neu_vect = [vector[x] for x in cont_neu_ind]
        cont_neg_vect = [vector[x] for x in cont_neg_ind]
        cont_pos_vect = [vector[x] for x in cont_pos_ind]
        neut_neu_vect = [vector[x] for x in neut_neu_ind]
        neut_neg_vect = [vector[x] for x in neut_neg_ind]
        neut_pos_vect = [vector[x] for x in neut_pos_ind]

############################################  1

    len1 = len(part_neu_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = part_neu_vect[0]
            tmp = operate_on_Narray(part_neu_vect[0], tmp[a+1], lambda x, y: x + y)

        tmp = operate_on_Narray(part_neu_vect[0], tmp[a+1], lambda x, y: x / len1)

        part_neu_vect = list(tmp)


    else:
        part_neu_vect = []

############################################  2

    len1 = len(part_neg_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = part_neg_vect[0]
            tmp = operate_on_Narray(part_neg_vect[0], tmp[a+1], lambda x, y: x + y)

        tmp = operate_on_Narray(part_neg_vect[0], tmp[a+1], lambda x, y: x / len1)

        part_neg_vect = list(tmp)


    else:
        part_neg_vect = []

############################################  3

    len1 = len(part_pos_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = part_pos_vect[0]
            tmp = operate_on_Narray(part_pos_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(part_pos_vect[0], tmp[a + 1], lambda x, y: x / len1)
        part_pos_vect = list(tmp)

    else:
        part_pos_vect = []

############################################  4

    len1 = len(cont_neu_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = cont_neu_vect[0]
            tmp = operate_on_Narray(cont_neu_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(cont_neu_vect[0], tmp[a + 1], lambda x, y: x / len1)
        cont_neu_vect = list(tmp)

    else:
        cont_neu_vect = []

############################################  5

    len1 = len(cont_neg_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = cont_neg_vect[0]
            tmp = operate_on_Narray(cont_neg_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(cont_neg_vect[0], tmp[a + 1], lambda x, y: x / len1)
        cont_neg_vect = list(tmp)

    else:
        cont_neg_vect = []

############################################  6

    len1 = len(cont_pos_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = cont_pos_vect[0]
            tmp = operate_on_Narray(cont_pos_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(cont_pos_vect[0], tmp[a + 1], lambda x, y: x / len1)
        cont_pos_vect = list(tmp)

    else:
        cont_pos_vect = []

############################################  7

    len1 = len(neut_neu_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = neut_neu_vect[0]
            tmp = operate_on_Narray(neut_neu_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(neut_neu_vect[0], tmp[a + 1], lambda x, y: x / len1)
        neut_neu_vect = list(tmp)

    else:
        neut_neu_vect = []

############################################  8

    len1 = len(neut_neg_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = neut_neg_vect[0]
            tmp = operate_on_Narray(neut_neg_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(neut_neg_vect[0], tmp[a + 1], lambda x, y: x / len1)

        neut_neg_vect = list(tmp)

    else:
        neut_neg_vect = []

############################################  9

    len1 = len(neut_pos_vect)
    if len1 != 0:
        for a in range(len1):
            tmp = neut_pos_vect[0]
            tmp = operate_on_Narray(neut_pos_vect[0], tmp[a + 1], lambda x, y: x + y)

        tmp = operate_on_Narray(neut_pos_vect[0], tmp[a + 1], lambda x, y: x / len1)

        neut_pos_vect = list(tmp)

    else:
        neut_pos_vect = []



    return [part_neu_vect, part_neg_vect, part_pos_vect, cont_neu_vect, cont_neg_vect, cont_pos_vect, neut_neu_vect, neut_neg_vect, neut_pos_vect]



def saveTraining():

    sert = trainVect()
    trnVect = open('trn_vect.vec', 'w')

    for i in sert:
        trnVect.write(str(i) + '\n')
