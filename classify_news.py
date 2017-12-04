from sklearn.feature_extraction.text import TfidfVectorizer
from stopWords import stopWrdList

def getTrnVect():
    # code to get the trained vectors

    import yaml

    str_trained_vect = open('trn_vect.vec', 'r').read().split('\n')

    str_trained_vect.pop(len(str_trained_vect)-1)


    trained_vect = []
    for i in str_trained_vect:
        trained_vect.append(yaml.load(i))


    del str_trained_vect, i

    return trained_vect


def classify_news(document):
    # code to vectorize news to classify

    from similarityMeasures import cos_sim

    vect_to_classify = []

    news = open(document, 'r').read()

    vect_to_classify.append(news)

    stop_words = stopWrdList()

    vectorizer = TfidfVectorizer(strip_accents='ascii', analyzer='word', stop_words=stop_words, max_features=100)

    X = vectorizer.fit_transform(vect_to_classify)
    vector = X.toarray()

    trained_vectors = getTrnVect()

    # get dim

    len_vector = len(vector[0])
    len_train = len(trained_vectors[0])

    vector = list(vector[0])
    if len_train > len_vector:
        for i in range(len_train - len_vector):
            vector.append(0)

    sim_vect = []
    for i in trained_vectors:
        sim_vect.append(cos_sim(vector, i))


    maxi = max(sim_vect)


    x = 0
    for i in sim_vect:
        if i == maxi:
            y = x
        x = x + 1

    part_neu_vect = 'This note has neutral emotions and it is related with the party'
    part_neg_vect = 'This note has negative emotions and it is related with the party'
    part_pos_vect = 'This note has positive emotions and it is related with the party'
    cont_neu_vect = 'This note has neutral emotions and it is related with the opposition'
    cont_neg_vect = 'This note has negative emotions and it is related with the opposition'
    cont_pos_vect = 'This note has positive emotions and it is related with the opposition'
    neut_neu_vect = 'This note has neutral emotions and it is not particularly related a political party'
    neut_neg_vect = 'This note has negative emotions and it is not particularly related a political party'
    neut_pos_vect = 'This note has positive emotions and it is not particularly related a political party'

    results = [part_neu_vect, part_neg_vect, part_pos_vect, cont_neu_vect, cont_neg_vect, cont_pos_vect, neut_neu_vect, neut_neg_vect, neut_pos_vect]

    print(results[y])
