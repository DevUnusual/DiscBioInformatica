#ALUNO: CARLOS MENESES GUIMARAES SOUSA - MATRICULA: 20179026483
import numpy as np #biblioteca para trabalhar com matrizes Necessario instalar, pode ser instalado caso tenha python instalado com o comando "pip install numpy"
import re #biblioteca para trabalhar com expressões regulares nativa

## gap mismatch match Parametros do algoritmo
gap = -3
mismatch = -1
match = 2

file = open("input.txt", "r") #abrindo o arquivo para leitura
data = file.read() #salvando em variavel
file.close() 

data = re.findall("[A-Z]+", data) #Regex para extrair a sequencia 1 e 2 do arquivo input.txt, funciona para arquivos de texto com as sequencias em letra Maiuscula
print(data)
compost = np.dtype([('horizontal',int),("diagonal",int),("vertical",int),("maior", int)]) 
bioType = np.dtype([("maiorValor", int),("direcao",(str,3))]) #Criando um tipo composto no numpy para servir na matriz e usar para guardar maiorValor e as direcoes
matriz = np.zeros((len(data[0])+1, len(data[1])+1), dtype=compost) #seq1 na linha e seq2 na coluna , np.zeros serve para criar a matriz[seq1][seq2] para facilitar a manipulação do algoritmo
matriz_aux = np.empty((len(data[0])+1, len(data[1])+1), dtype=(str,3)) #matriz auxiliar para guardar os valores e direcoes
matriz[0][0] = 0
for i in range(1,len(data[0])+1): #Preenchendo a primeira coluna e a primeira linha com os gaps de cada célula
    matriz[i][0] = gap * i
    if i <= len(data[1]):
        matriz[0][i] = gap * i

for i in range(1,len(data[0])+1):
    for j in range(1,len(data[1])+1):
        caminho = '' ##d-diagonal, v-vertical, h-horizontal
        if data[0][i-1] == data[1][j-1]: #Caso seja match verifica o match e os gaps
            maior_resultado = max(matriz[i-1][j][3] + gap, matriz[i][j-1][3] + gap, matriz[i-1][j-1][3] + match) #atribui o maior valor dos 3 a variavel
            if maior_resultado == matriz[i-1][j][3] + gap: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'v'
            if maior_resultado == matriz[i][j-1][3] + gap: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'h'
            if maior_resultado == matriz[i-1][j-1][3] + match: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'd'
            matriz[i][j] = maior_resultado #atribui o maior valor a matriz
            matriz[i][j][0] = matriz[i][j-1][3] + gap #atribui o maior valor a matriz
            matriz[i][j][1] = matriz[i-1][j-1][3] + match #atribui o maior valor a matriz
            matriz[i][j][2] = matriz[i-1][j][3] + gap #atribui o maior valor a matriz
            matriz_aux[i][j] = caminho #atribui a direcao a matriz

        else: #Caso nao seja match testa o mismatch e os gaps vertical e horizontal
            maior_resultado = max(matriz[i-1][j][3] + gap, matriz[i][j-1][3] + gap, matriz[i-1][j-1][3] + mismatch)
            if maior_resultado == matriz[i-1][j][3] + gap: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'v'
            if maior_resultado == matriz[i][j-1][3] + gap: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'h'
            if maior_resultado == matriz[i-1][j-1][3] + mismatch: #caso encontre um com valor igual concatena a variavel caminho com a direcao
                caminho += 'd'
            matriz[i][j] = maior_resultado
            matriz[i][j][0] = matriz[i][j-1][3] + gap #atribui o maior valor a matriz
            matriz[i][j][1] = matriz[i-1][j-1][3] + mismatch #atribui o maior valor a matriz
            matriz[i][j][2] = matriz[i-1][j][3] + gap #atribui o maior valor a matriz
            matriz_aux[i][j] = caminho
        
backtrace = [[],[]] #guardas as letras para fazer a inversao no final e gerar o resultado do alinhamento
topo = [len(data[0]), len(data[1])] #variavel que pega o tamanho das sequencias para percorrer a tabela gerada

while topo[0] + topo[1] != 0: #enquanto ambos os topos nao forem zero o while continua a recuar até chegar o fim do backtrace
    y_seq = topo[0]
    x_seq = topo[1]
    if y_seq == 0 or x_seq == 0: #verifica se o backtrace enconsta na coluna de gaps ou linha de gaps, a primeira coluna ou a primeira linha da tabela
        if y_seq == 0: #percorre a coluna de gaps
            backtrace[0].append("-")
            backtrace[1].append(data[1][x_seq-1])
            topo[1] -= 1
        elif x_seq == 0: #percorre a linha de gaps
            backtrace[0].append(data[0][y_seq-1])
            backtrace[1].append("-")
            topo[0] -= 1 
    elif 'v' in matriz_aux[y_seq][x_seq]: 
        #verifica os caminhos em que a celula pode ir de acordo com a string no segundo campo apos identificar um caminho ela adiciona ao backtrace e passa para a proxima celula 
        backtrace[0].append(data[0][y_seq-1])
        backtrace[1].append("-")
        topo[0] -= 1 #movimento na vertical na matriz
    elif 'd' in matriz_aux[y_seq][x_seq]:
        #verifica os caminhos em que a celula pode ir de acordo com a string no segundo campo apos identificar um caminho ela adiciona ao backtrace e passa para a proxima celula 
        backtrace[0].append(data[0][y_seq-1])
        backtrace[1].append(data[1][x_seq-1])
        topo[0] -= 1 #movimento na diagonal na matriz subtraindo 1 da linha e coluna
        topo[1] -= 1 #movimento na diagonal na matriz subtraindo 1 da linha e coluna
    elif 'h' in matriz_aux[y_seq][x_seq]:
        #verifica os caminhos em que a celula pode ir de acordo com a string no segundo campo apos identificar um caminho ela adiciona ao backtrace e passa para a proxima celula 
        backtrace[0].append("-")
        backtrace[1].append(data[1][x_seq-1])
        topo[1] -= 1 #movimento na horizontal na matriz

file = open("output.txt", "w")
for i in backtrace[0][::-1]: #for percorrendo o primeiro array do backtrace de tras para frente e escrevendo no arquivo
    file.write(i)
file.write("\n")
for i in backtrace[1][::-1]: #for percorrendo o segundo array do backtrace de tras para frente e escrevendo no arquivo
    file.write(i)
file.write("\n")
file.write((f"Score: {matriz[len(data[0])][len(data[1])][0]}\nmatch: {match}\ngap: {gap}\nmismatch: {mismatch}\n")) #salvando os resultados
file.close()

#essa parte do codigo serve para imprimir a tabela afin de debugar
file = open("output.txt", "a")
np.savetxt(file, matriz[::-1], fmt="%-20s",delimiter="||")