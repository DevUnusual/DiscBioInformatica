import numpy as np
import re
## gap mismatch match
gap = -2
mismatch = -1
match = 3



file = open("input.txt", "r")
data = file.read()
file.close()

data = re.findall("([A-Za-z]+)", data)

matriz = np.zeros((len(data[0])+1, len(data[1])+1), dtype=list)

for i in range(1,len(data[0])+1):
    matriz[i][0] = gap * i
    if i <= len(data[1]):
        matriz[0][i] = gap * i


for i in range(1,len(data[0])+1):
    for j in range(1,len(data[1])+1):
        caminho = '' ##d-diagonal, v-vertical, h-horizontal
        if data[0][i-1] == data[1][j-1]:
            maior_resultado = max(matriz[i-1][j-1][0] + match, matriz[i-1][j][0] + gap, matriz[i][j-1][0] + gap)
            if maior_resultado == matriz[i-1][j] + gap:
                caminho += 'v'
            if maior_resultado == matriz[i][j-1] + gap:
                caminho += '-h'
            if maior_resultado == matriz[i-1][j-1] + match:
                caminho += '-d'
            
            matriz[i][j] = [maior_resultado, caminho]
        else:
            maior_resultado = max(matriz[i-1][j][0] + gap, matriz[i][j-1][0] + gap, matriz[i-1][j-1][0] + mismatch)
            if maior_resultado == matriz[i-1][j] + gap:
                caminho += 'v'
            if maior_resultado == matriz[i][j-1] + gap:
                caminho += '-h'
            if maior_resultado == matriz[i-1][j-1] + mismatch:
                caminho += '-d'
            matriz[i][j] = [maior_resultado, caminho]









def save_matriz(matriz, caminho):
    file = open("output.txt", "w")
    np.savetxt(file, matriz, fmt="%+4d",delimiter="|")
    print(matriz)
    np.savetxt(file, caminho)


save_matriz(matriz, caminho)