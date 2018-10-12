##Initialisation
from os import chdir
chdir('c:/users/paula/desktop/MINES NANCY/INFO/TD1')

objetFichier=open('p022_names.txt', 'r')
L=[]
for e in objetFichier:
    L.append(e)
objetFichier.close()

L=L[0].split(',')

for i in range(len(L)):
    L[i]=L[i].replace('"','')


lettreValeur={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

##Tri de L

LTri=sorted(L)

##Fonctions
def valeurMot(s):
    res=0
    for e in s:
        res+=lettreValeur[e]
    return res

##Solution
res=0
for i in range(len(LTri)):
    res+=(i+1)*valeurMot(LTri[i])
print(res)