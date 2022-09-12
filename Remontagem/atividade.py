import re
from igraph import *
file = open("kmerAtividade.txt", "r")
kmer = re.findall('[ATCG]{3}', file.read())

print(kmer)

# separar em tuplas, juntar iguais fazer o caminho

def separarTuplas(kmer):
    contador = 1
    tuplas = []
    for i in kmer:
        tuplas.append([i[0:len(i)-1],i[1:len(i)],contador])
        contador += 1
    #print(tuplas)
    return tuplas

def paresIguais(tuplas):
    for i in tuplas:
        for j in tuplas:
            #print("i,j",i,j)
            if i[2] == j[2]:
                continue
            elif i[0] in j:
                i.append([j[0],j[1]])
                tuplas.pop(tuplas.index(j)) 
            elif i[1] in j:
                i.append([j[0],j[1]])
                tuplas.pop(tuplas.index(j))
    return tuplas
                
            
print(paresIguais(separarTuplas(kmer)))
