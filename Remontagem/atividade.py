from importExport import *
import numpy as np
from numpy.lib import recfunctions as rfn

kmer = kmerImport()
kmer = np.array(kmer)

print(kmer)

# separar em tuplas, juntar iguais fazer o caminho

def separarTuplas(kmer):
    contador = 0
    tuplas = []
    for i in sorted(kmer):
        tuplas.append((i[:len(i)-1], i[1:len(i)], contador)) # kmer-1, -1kmer, posicao tabela
        contador += 1
    #print(tuplas, 'tuplas')
    return np.array(tuplas)

def makeTable(tuplas, kmers, nKmers): #####CONTAR TODOS OS KMERS E FAZER UMA TABELA COM TAMANHO TOTAL DELES SEM REPETIDOS NO MOMENTO TEM NOMES REPETIDOS NA TABELA
    tabela = np.zeros((nKmers,nKmers),dtype=int)
    for kmer1 in tuplas:
        tabela[int(kmers.index(kmer1[0]))][int(kmers.index(kmer1[1]))] += 1
    print(tabela)
    return tabela

def lenkmers(tuplas):
    kmers = 0
    visitados = []
    for i in tuplas:
        if i[0] not in visitados:
            kmers += 1
            visitados.append(i[0])
        if i[1] not in visitados:
            kmers += 1
            visitados.append(i[1])
    #print('kmers', kmers)
    print('visitados', visitados) # AT TC TG TT CA CC GA AC GC 
    return (visitados, kmers)

def percorreTabela(tabela, kmers):
    linha = 0
    kmerProximo = []
    for x in range(len(kmers)):
        kmerProximo.append([])

    for i in tabela:
        #print('i',i, 'linha', linha, 'pos', i.nonzero()[0])
        if not i.any(where= 1):
            print(f'--> {kmers[linha]} final do caminho')
            final = linha
        print(f'lista {kmerProximo} len {len(kmerProximo)} acessando 0 {kmerProximo[0]}')
        for k in i.nonzero()[0]:
            print(f'{kmers[linha]} apontando para {kmers[k]}')
            value = tabela [linha][k]
            for j in range(value):
                kmerProximo[int(kmers.index(kmers[k]))].append(linha)
        linha = linha + 1
    return (final, kmerProximo)

def caminho(final, ligacoes, visitados):
    passoApasso = []
    while ligacoes != []:
        passoApasso.append(final)
        if len(ligacoes[final]) > 1:
            final = ligacoes[final].pop()
        final = ligacoes[final]
        ligacoes.remove(final)
        ligacoes = ligacoes.insert()

tuplas = separarTuplas(kmer)
(visitados, kmers) = lenkmers(tuplas)
tabela = makeTable(tuplas, visitados, kmers)
(final, ligacoes) = percorreTabela(tabela, visitados)
way = caminho( final, ligacoes, visitados)

print('ligacoes', ligacoes)
print('way', way)

