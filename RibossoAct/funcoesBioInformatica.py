import re

def read(caminho= "dna.txt"):
    try:
        file = open(caminho, "r")
        dnaRead = file.readlines() #Lendo linha do arquivo
        dnaRead = [element.upper().strip() for element in dnaRead] #fazendo tratamento no arquivo convertendo todas as string para maiusculo
        dnaRead = list(filter(None, dnaRead)) #tirando linhas vazias caso tenha
        dnaFormated = []
        if dnaRead[0].find("DNA") != -1: #caso encontre DNA na primeira linha ignorar até chegar na cadeia de nucleotideos
            for i in dnaRead[1:]:
                if i.find("A") or i.find("T") or i.find("G") or i.find("C"):
                    dnaFormated.append(i)
        elif dnaRead[0].find("A") or dnaRead[0].find("T") or dnaRead[0].find("G") or dnaRead[0].find("C"):
            dnaFormated.append(dnaRead[0])

        return dnaFormated

    except FileNotFoundError as e:
        print(e)
    except :
        print("houve algum erro no codigo")

def dnaTranscript(dnaFormated):
    dict = {"A": "T", "T": "U", "G":"C", "C": "G"}
    rna = ""
    for i in range(len(dnaFormated)):
        for j in range(len(dnaFormated[i])):
            rna = rna + dict.get(dnaFormated[i][j])

    return rna

def readRna():
    try:
        file = open("rna.txt", "r")
        rnaRead = file.readlines() #Lendo linha do arquivo
        rnaRead = [element.upper().strip() for element in rnaRead] #fazendo tratamento no arquivo convertendo todas as string para maiusculo
        rnaRead = list(filter(None, rnaRead)) #tirando linhas vazias caso tenha
        return rnaRead[0]
    except FileNotFoundError as e:
        print(e)
    except :
        print("houve algum erro no codigo")