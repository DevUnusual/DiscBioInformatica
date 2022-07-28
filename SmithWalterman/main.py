import numpy as np
import re
## gap mismatch match
gap = -3
mismatch = -1
match = 3



file = open("input.txt", "r")
data = file.read()
file.close()

data = re.findall("([A-Za-z]+)", data)

matriz = np.empty((len(data[0])+1, len(data[1])+1), dtype=int) #seq1 na linha e seq2 na coluna
matriz_auxiliar = np.empty((len(data[0])+1, len(data[1])+1), dtype=(str, 4))

matriz[0][0] = 0
for i in range(1,len(data[0])+1):
    matriz[i][0] = gap * i
    if i <= len(data[1]):
        matriz[0][i] = gap * i

for i in range(1,len(data[0])+1):
    for j in range(1,len(data[1])+1):
        caminho = '' ##d-diagonal, v-vertical, h-horizontal
        if data[0][i-1] == data[1][j-1]:
            maior_resultado = max(matriz[i-1][j] + gap, matriz[i][j-1] + gap, matriz[i-1][j-1] + match)
            if maior_resultado == matriz[i-1][j] + gap:
                caminho += 'v'
            if maior_resultado == matriz[i][j-1] + gap:
                caminho += 'h'
            if maior_resultado == matriz[i-1][j-1] + match:
                caminho += 'd'
            matriz[i][j] = maior_resultado
            matriz_auxiliar[i][j] = caminho

        else:
            maior_resultado = max(matriz[i-1][j] + gap, matriz[i][j-1] + gap, matriz[i-1][j-1] + mismatch)
            if maior_resultado == matriz[i-1][j] + gap:
                caminho += 'v'
            if maior_resultado == matriz[i][j-1] + gap:
                caminho += 'h'
            if maior_resultado == matriz[i-1][j-1] + mismatch:
                caminho += 'd'
            matriz[i][j] = maior_resultado
            matriz_auxiliar[i][j] = caminho
        
        #print(f"{maior_resultado} : {matriz[i-1][j] + gap} / {matriz[i][j-1] + gap} / {matriz[i-1][j-1] + mismatch} / {matriz[i-1][j-1] + match} - {caminho}")

backtrace = [[],[]]
topo = [len(data[0]), len(data[1])]

while matriz[topo[0]][topo[1]] != 0:
    y_seq = topo[0]
    x_seq = topo[1]
    if y_seq == 0 or x_seq == 0:
        if y_seq == 0:
            backtrace[0].append("-")
            backtrace[1].append(data[1][x_seq-1])
            topo[1] -= 1
        elif x_seq == 0:
            backtrace[0].append(data[0][y_seq-1])
            backtrace[1].append("-")
            topo[0] -= 1
        
    elif 'd' in matriz_auxiliar[y_seq][x_seq]:
        backtrace[0].append(data[0][y_seq-1])
        backtrace[1].append(data[1][x_seq-1])
        topo[0] -= 1
        topo[1] -= 1
    elif 'v' in matriz_auxiliar[y_seq][x_seq]:
        backtrace[0].append(data[0][y_seq-1])
        backtrace[1].append("-")
        topo[0] -= 1
    elif 'h' in matriz_auxiliar[y_seq][x_seq]:
        backtrace[0].append("-")
        backtrace[1].append(data[1][x_seq-1])
        topo[1] -= 1


##print(backtrace[0])
#print(backtrace[1])

resultado = np.full((2, len(backtrace[0])),fill_value=(backtrace[0], backtrace[1]),dtype=str)
print(resultado)





def save_matriz(resultado):
    file = open("output.txt", "w")
    #np.savetxt(file, resultado, fmt="%s")
    for i in resultado[0][::-1]:
        file.write(i)
    file.write("\n")
    for i in resultado[1][::-1]:
        file.write(i)
    file.write("\n")
    file.close()

#print(matriz_auxiliar)
save_matriz(resultado)

file = open("output.txt", "a")
np.savetxt(file, matriz[::-1], fmt="%+4s",delimiter="|")
file.write("----------------------------------------------------------------------\n")
np.savetxt(file, matriz_auxiliar[::-1], fmt="%+4s",delimiter="|")
