import funcoesBioInformatica as fBio
import re
#aug:metionina cua:Leucina cgu:arginina agc:serina uag
geneticCode = {'UUU' : 'Fenilalanina' , 'UUC' : 'Fenilalanina' , 'UUA' : 'Leucina' , 'UUG' : 'Leucina', 'CUU' : 'Leucina' , 'CUC' : 'Leucina' , 'CUA' : 'Leucina' , 'CUG' : 'Leucina', 
               'AUU' : 'Isoleucina' , 'AUC' : 'Isoleucina' , 'AUA' : 'Isoleucina', 'AUG' : 'Metionina', 'GUU' : 'Valina', 'GUC' : 'Valina' , 'GUA' : 'Valina' , 'GUG' : 'Valina' ,
               'UCU' : 'Serina' , 'UCC' : 'Serina' , 'UCA' : 'Serina' , 'UCG' : 'Serina' , 'CCU' : 'Prolina' , 'CCC' : 'Prolina' , 'CCA' : 'Prolina' , 'CCG' : 'Prolina' ,
               'ACU' : 'Treonina' , 'ACC' : 'Treonina' , 'ACA' : 'Treonina' , 'ACG' : 'Treonina' , 'GCU' : 'Alanina' , 'GCC' : 'Alanina' , 'GCA' : 'Alanina' , 'GCG' : 'Alanina' ,
               'UAU' : 'Tirosina' , 'UAC' : 'Tirosina' , 'UAA' : False , 'UAG' : False , 'CAU' : 'Histidina' , 'CAC' : 'Histidina' , 'CAA' : 'Glutamina' , 'CAG' : 'Glutamina' ,
               'AAU' : 'Asparagina' , 'AAC' : 'Asparagina' , 'AAA' : 'Lisina' , 'AAG' : 'Lisina' , 'GAU' : 'Ácido aspártico' , 'GAC' : 'Ácido aspártico' , 'GAA' : 'Ácido glutâmico' , 'GAG' : 'Ácido glutâmico' ,
               'UGU' : 'Cisteína' , 'UGC' : 'Cisteína' , 'UGA' : False , 'UGG' : 'Triptofano' , 'CGU' : 'Arginina' , 'CGC' : 'Arginina' , 'CGA' : 'Arginina' , 'CGG' : 'Arginina' ,
               'AGU' : 'Serina' , 'AGC' : 'Serina' , 'AGA' : 'Arginina' , 'AGG' : 'Arginina' , 'GGU' : 'Glicina' , 'GGC' : 'Glicina' , 'GGA' : 'Glicina' , 'GGG' : 'Glicina' }

def main():
    rna = fBio.readRna()
    rnaCodons = re.findall("([A-Z][A-Z][A-Z])", rna)
    rnaCodons.append("END")
    initialPosition = 0
    atualPosition = 0
    aminoacidos = []
    tempAminoacidos = []
    while rnaCodons[atualPosition] != "END":
        for i in range(atualPosition,len(rnaCodons[atualPosition:])):
            temp = rnaCodons[i]
            if temp == 'AUG':
                initialPosition = i
                atualPosition = i
                break
            elif temp == 'END':
                print("Nao foi encontrado nenhum codon que inicia o processo de criacao da proteina")
        for i in rnaCodons[initialPosition:]:
            temp = geneticCode.get(i)
            if rnaCodons[atualPosition] == "END":
                break
            if temp != False:
                tempAminoacidos.append(temp)
                atualPosition += 1
            else:
                tempAminoacidos.append("stop")
                aminoacidos.append(tempAminoacidos)
                tempAminoacidos = []
                atualPosition += 1
                break
    print("sequencias de aminoacidos encontradas:")
    for i in aminoacidos:
        print(i)
    print("Imprimindo no arquivo proteinas.txt")
    resultado = open("proteinas.txt", "w")
    resultado.write("Proteinas:\n")
    for i in aminoacidos:
        resultado.write(str(i)+"\n")

main()