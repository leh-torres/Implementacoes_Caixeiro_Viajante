from itertools import permutations
import time

def tsp(matriz):

    numCidades = len(matriz)
    cidades = list(range(1, numCidades))
    
    minCost = float('inf')
    melhorCam = None

    for perm in permutations(cidades):
        currCidade = 0
        currCusto = 0

        cam = [0] + list(perm)

        for cid in perm:
            currCusto += matriz[currCidade][cid]
            currCidade = cid

        currCusto += matriz[currCidade][0]  # Retorno à cidade inicial

        if currCusto < minCost:
            minCost = currCusto  # Atualiza o custo mínimo
            melhorCam = cam      # Atualiza a melhor rota encontrada

    melhorCam = melhorCam + [0]
    
    print("Distância mínima:", minCost)
    print("Melhor caminho:", melhorCam)

m_dist = [[0, 34, 16, 16, 13, 34, 39, 16, 36, 11, 4, 25, 9, 16], [34, 0, 20, 4, 46, 20, 15, 1, 44, 12, 21, 39, 22, 17], [16, 20, 0, 27, 40, 30, 34, -1, 35, 9, 7, 11, 29, 17], [16, 4, 27, 0, 2, 28, 36, 33, 37, 28, 27, 37, 39, 20], [13, 46, 40, 2, 0, 45, 46, 41, 23, 18, 34, 15, 22, 50], [34, 20, 30, 28, 45, 0, 33, 26, 27, 31, 35, 48, 48, 42], [39, 15, 34, 36, 46, 33, 0, 31, 40, 12, 2, 26, 38, 14], [16, 1, -1, 33, 41, 26, 31, 0, 24, 15, 24, 14, 27, 48], [36, 44, 35, 37, 23, 27, 40, 24, 0, 4, 7, 26, 23, 14], [11, 12, 9, 28, 18, 31, 12, 15, 4, 0, 16, 26, 42, 46], [4, 21, 7, 27, 34, 35, 2, 24, 7, 16, 0, 29, 1, 2], [25, 39, 11, 37, 15, 48, 26, 14, 26, 26, 29, 0, 15, 39], [9, 22, 29, 39, 22, 48, 38, 27, 23, 42, 1, 15, 0, 38], [16, 17, 17, 20, 50, 42, 14, 48, 14, 46, 2, 39, 38, 0]]

print(m_dist, type(m_dist))
inicio = time.time()
tsp(m_dist)
fim = time.time()
print(f'Tempo: {fim-inicio}')