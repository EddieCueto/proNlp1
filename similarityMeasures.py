"""
Created on Mon Apr 17 09:34:40 2017
functions to calculate the similarity measure of two real vectors
@author: nlp
"""
# The cosine measure definition
def cos_sim(vect1, vect2):
    if (len(vect1) == len(vect2)):
        vect3 = []
        for x in range(0, len(vect1)):
            vect3.append(0)
            
        for x in range(0, len(vect1)):
            vect3[x] = vect1[x] * vect2[x]
    
        n1 = norm(vect1)
        n2 = norm(vect2)
    
        return sum(vect3)/(n1*n2)
        
    else:
       return 0
       
# Norm of vector
def norm(vect):
    import math as mth
    vect1 = []
    for x in range(0, len(vect)):
        vect1.append(0)
            
    for x in range(0, len(vect)):
        vect1[x] = vect[x] * vect[x]    
            
    return mth.sqrt(sum(vect1))

# Jacard similarity
def jac_sim(set_A,set_B):
    if (str(type(set_A)) and str(type(set_B))) == "<class 'set'>":
        if set_A == set_B:
            return len(set_A & set_B)/len(set_A | set_B)
        else:
            return len(set_A & set_B)/len((set_A | set_B) - (set_A & set_B))
    else:
        print('One of the inputs not of type set')
        