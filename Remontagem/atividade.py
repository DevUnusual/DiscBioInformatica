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
        # kmer-1, -1kmer, posicao tabela
        tuplas.append((i[:len(i)-1], i[1:len(i)], contador))
        contador += 1
    # print(tuplas, 'tuplas')
    return np.array(tuplas)


# CONTAR TODOS OS KMERS E FAZER UMA TABELA COM TAMANHO TOTAL DELES SEM REPETIDOS NO MOMENTO TEM NOMES REPETIDOS NA TABELA
def makeTable(tuplas, kmers, nKmers):
    tabela = np.zeros((nKmers, nKmers), dtype=int)
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
    # print('kmers', kmers)
    # print('visitados', visitados)  # AT TC TG TT CA CC GA AC GC
    return (visitados, kmers)


def percorreTabela(tabela, kmers):
    linha = 0
    kmerProximo = []
    for x in range(len(kmers)):
        kmerProximo.append([])

    for i in tabela:
        # print('i',i, 'linha', linha, 'pos', i.nonzero()[0])
        if not i.any(where=1):
            # print(f'--> {kmers[linha]} final do caminho')
            final = linha
        # print(
            # f'lista {kmerProximo} len {len(kmerProximo)} acessando 0 {kmerProximo[0]}')
        for k in i.nonzero()[0]:
            # print(f'{kmers[linha]} apontando para {kmers[k]}')
            value = tabela[linha][k]
            for j in range(value):
                kmerProximo[int(kmers.index(kmers[linha]))].append(k)
        linha = linha + 1
    # print(kmerProximo, 'kmerProximo')
    return (final, kmerProximo)


def caminho(final, ligacoes, visitados):
    passoApasso = []
    passoApasso.append(final)
    while np.array(ligacoes, dtype=object).size > 0:
        for liglist in ligacoes:
            for unidade in liglist:
                if unidade == final:
                    kmerAnterior = ligacoes.index(liglist)
                    ligacoes[kmerAnterior].remove(unidade)
                    passoApasso.append(kmerAnterior)
                    final = kmerAnterior
                    # print(f'passo a passo {passoApasso}')
                    # print(f'ligacoes {ligacoes}')
                    continue
                # print(f'{unidade} <- unidade, final -> {final}')

    # print(passoApasso, 'passo a passo')
    return passoApasso


def imprimirCaminho(caminho, kmers):
    resultado = ""
    resultado += kmers[caminho[0]]
    for i in caminho[1:]:
        resultado += kmers[i][-1]

    return resultado


tuplas = separarTuplas(kmer)
(visitados, kmers) = lenkmers(tuplas)
tabela = makeTable(tuplas, visitados, kmers)
(final, ligacoes) = percorreTabela(tabela, visitados)
way = caminho(final, ligacoes, visitados)
resultadoFinal = imprimirCaminho(way[:: -1], visitados)
#print('ligacoes', ligacoes)
print('way', way)
print('resultadoFinal', resultadoFinal, len(resultadoFinal))

kmerExport(resultadoFinal)
