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

matriz = np.empty((len(data[0])+1, len(data[1])+1), dtype=int)
matriz_auxiliar = np.empty((len(data[0])+1, len(data[1])+1), dtype=str)

for i in range(1,len(data[0])+1):
    matriz[i][0] = gap * i
    if i <= len(data[1]):
        matriz[0][i] = gap * i

caminho = []

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
        
        print(f"{maior_resultado} : {matriz[i-1][j] + gap} / {matriz[i][j-1] + gap} / {matriz[i-1][j-1] + mismatch} / {matriz[i-1][j-1] + match} - {caminho}")









def save_matriz(matriz):
    file = open("output.txt", "w")
    np.savetxt(file, matriz, fmt="%+4s",delimiter="|")
    print(matriz)

print(matriz_auxiliar)
save_matriz(matriz_auxiliar)