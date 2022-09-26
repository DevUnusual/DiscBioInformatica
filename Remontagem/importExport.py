def kmerImport(location = "kmer.txt"):
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
    kmerfile = open("kmer.txt", "w")
    kmerfile.write(way)