def kmerImport(location="Atividade_9.COMPUTACAO.PROVA.Vale 10.composicao_1_Bioinformaticas_size_30000_k_50.txt"):
    kmerfile = open(location, "r")
    kmer = kmerfile.read()
    kmer = kmer.split(',')
    verify(len(kmer[0]), kmer)
    print("Kmers importados com sucesso")
    return kmersOrdenados(kmer)


def verify(tam, kmer):
    if kmer[-1] == '':
        kmer.pop()
    for i in kmer:
        if len(i) != tam:
            print("Error: sequencia de kmers invalida")
            exit()


def kmersOrdenados(kmer):
    kmer.sort()
    return kmer


def kmerExport(way):
    kmerfile = open("CarlosSousa.txt", "w")
    kmerfile.write(way)
