import funcoesBioInformatica as fBio
import re
#aug:metionina cua:Leucina cgu:arginina agc:serina uag
geneticCode = {'UUU' : 'Fenilalanina' , 'UUC' : 'Fenilalanina' , 'UUA' : 'Leucina' , 'UUG' : 'Leucina', 'CUU' : 'Leucina' , 'CUC' : 'Leucina' , 'CUA' : 'Leucina' , 'CUG' : 'Leucina', 
               'AUU' : 'Isoleucina' , 'AUC' : 'Isoleucina' , 'AUA' : 'Isoleucina', 'AUG' : 'Metionina', 'GUU' : 'Valina', 'GUC' : 'Valina' , 'GUA' : 'Valina' , 'GUG' : 'Valina' ,
               'UCU' : 'Serina' , 'UCC' : 'Serina' , 'UCA' : 'Serina' , 'UCG' : 'Serina' , 'CCU' : 'Prolina' , 'CCC' : 'Prolina' , 'CCA' : 'Prolina' , 'CCG' : 'Prolina' ,
               'ACU' : 'Treonina' , 'ACC' : 'Treonina' , 'ACA' : 'Treonina' , 'ACG' : 'Treonina' , 'GCU' : 'Alanina' , 'GCC' : 'Alanina' , 'GCA' : 'Alanina' , 'GCG' : 'Alanina' ,
               'UAU' : 'Tirosina' , 'UAC' : 'Tirosina' , 'UAA' : "OCRE" , 'UAG' : "AMBAR" , 'CAU' : 'Histidina' , 'CAC' : 'Histidina' , 'CAA' : 'Glutamina' , 'CAG' : 'Glutamina' ,
               'AAU' : 'Asparagina' , 'AAC' : 'Asparagina' , 'AAA' : 'Lisina' , 'AAG' : 'Lisina' , 'GAU' : 'Ácido aspártico' , 'GAC' : 'Ácido aspártico' , 'GAA' : 'Ácido glutâmico' , 'GAG' : 'Ácido glutâmico' ,
               'UGU' : 'Cisteína' , 'UGC' : 'Cisteína' , 'UGA' : "OPALA" , 'UGG' : 'Triptofano' , 'CGU' : 'Arginina' , 'CGC' : 'Arginina' , 'CGA' : 'Arginina' , 'CGG' : 'Arginina' ,
               'AGU' : 'Serina' , 'AGC' : 'Serina' , 'AGA' : 'Arginina' , 'AGG' : 'Arginina' , 'GGU' : 'Glicina' , 'GGC' : 'Glicina' , 'GGA' : 'Glicina' , 'GGG' : 'Glicina' }

def main():
    rna = fBio.readRna()
    rnaCodons = re.findall("([A-Z][A-Z][A-Z])", rna) #regex que separa o rna em grupo de 3 e devolve uma lista
    cad_aminoacidos = []
    start = False
    for i in rnaCodons:
        if i == "AUG":
            start = True
            cad_aminoacidos.append(geneticCode.get(i))
            continue
        if i == "UAA" or i == "UAG" or i == "UGA":
            cad_aminoacidos.append(geneticCode.get(i))
            break
        if start:
            cad_aminoacidos.append(geneticCode.get(i))
    print("Imprimindo no arquivo Cadeia_de_aminoacidos.txt")
    resultado = open("cadeia_de_aminoacidos.txt", "w")
    resultado.write(str(cad_aminoacidos))

main()