from heapq import heappush, heappop,heapify
from collections import defaultdict

texte = "Bienvenue"
frequence = defaultdict(int)
#définir le nomre d'occurence
for lettre in texte:
    frequence[lettre]+=1

tas = [(occ, lettre,{}) for (lettre, occ) in frequence.items()]
heapify(tas)

def IsFirstChild(noeud,dico):
    if len(noeud)==0:
        return dico
    else:
        return noeud
#Construit l'arbre:
while len(tas) >= 2:

    occ1, noeud1,dic1 = heappop(tas) # noeud de plus petit poids occ1
    occ2, noeud2,dic2 = heappop(tas) # noeud de deuxième plus petit poids occ2
    noeud1=IsFirstChild(noeud1,dic1)
    noeud2=IsFirstChild(noeud2,dic2)

    parents = occ1+occ2
    if occ1 < occ2:
        dico={"0":noeud1,"1":noeud2}
    else:
        dico={"0":noeud2,"1":noeud1}
    tas.append((occ1 + occ2, "",dico))


dic =tas[0][2]
def code(previousCode,dico,finaldico):
    for elem in dico:
        if(type(dico[elem])==dict):

            finalcode=previousCode+elem

            finaldico=code(finalcode,dico[elem],finaldico)
        else:
            finalcode=previousCode+elem
            finaldico[dico[elem]]=finalcode
    return finaldico


def convertTo(dicoCode,texte):
    binaryTxt=""
    for lettre in texte:
        binaryTxt+=dicoCode[lettre]
    return binaryTxt

def unconvert(dicoCode,binary):
    dictionary = {v: k for k, v in dicoCode.items()}
    res = ""
    while binary:
        for k in dictionary:
            if binary.startswith(k):
                res += dictionary[k]
                binary = binary[len(k):]
    return res

dicoCode=code("",dic,{}) #code attribué à chaque caractère
print('Texte :',texte)
print('Arbre :',tas[0])
print('Conversion en binaire huffman :',convertTo(dicoCode,texte)) #conversion en binaire huffman
print('déconversion :',unconvert(dicoCode,convertTo(dicoCode,texte))) #déconversion
