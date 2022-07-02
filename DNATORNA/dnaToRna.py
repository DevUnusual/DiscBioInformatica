import argparse
import funcoesBioInformatica as fBio

def main():
    parser = argparse.ArgumentParser(description = "Programa para transcrição de dna para rna.")
    parser.add_argument("-f", "--file", help = "local do arquivo.\n o arquivo tambem pode ser inserido no mesmo diretorio do programa e renomeado para dna.txt")
    parser.add_argument("-o", "--output", help = "Nome do arquivo de saida.\n Caso o argumento fique em branco vai ser gerado o arquivo rna.txt", default="rna.txt", type= str)

    args = parser.parse_args()

    if args.file is None:
        dnaFormated = fBio.read()
        rna = fBio.dnaTranscript(dnaFormated)
        output = open(args.output, "w")
        output.write("RNA trascrito a partir do DNA:\n" + rna)

    else:
        args.file = args.file.replace("\\", "\\\\") #tratando as barras para ser possivel acessar o arquivo
        dnaFormated = fBio.read(args.file) #abrindo arquivo passado por argumento
        #------------------- Arquivo lido e formatado para devolver uma lista de dna organizado ----------------------------------
        rna = fBio.dnaTranscript(dnaFormated) #funcao que transcreve o dna em rna
        output = open(args.output, "w") #escrever em arquivo a traducao
        output.write("RNA trascrito a partir do DNA:\n" + rna) 
        

main()