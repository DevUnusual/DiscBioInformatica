from more_itertools import iterate
import funcoesBioInformatica as fBio
import re
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
    initialPosition = 0
    atualPosition = 0
    iterate = 0
    amminoacidos = []
    tempAminoacidos = []
    while iterate < len(rnaCodons):
        for i in range(len(rnaCodons[atualPosition:])):
            if rnaCodons[i] == 'AUG':
                initialPosition = i
                iterate = i
                break
            elif rnaCodons[i] == 'END':
                print("Nao foi encontrado nenhum codon que inicia o processo de criacao da proteina")
        for i in rnaCodons[initialPosition:]:
            temp = geneticCode.get(i)
            if rnaCodons[iterate] == "END":
                iterate += 1
                break
            if temp != False:
                tempAminoacidos.append(temp)
                iterate += 1
            else:
                amminoacidos.append(tempAminoacidos)
                iterate += 1
                break
    print(amminoacidos)

main()