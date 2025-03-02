import numpy as np
import random
import time

def gerar_matriz_adjacencia(n):
    matriz = np.random.randint(10, 100, size=(n, n))
    np.fill_diagonal(matriz, 0)
    return matriz

def encontrar_menor_aresta(matriz):
    n = len(matriz)
    menor = float('inf')
    u, v = -1, -1
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] < menor:
                menor = matriz[i][j]
                u, v = i, j
    return u, v

def inserir_mais_barata(matriz):
    n = len(matriz)
    visitados = set()
    caminho = []
    
    u, v = encontrar_menor_aresta(matriz)
    caminho.extend([u, v])
    visitados.update([u, v])
    
    while len(caminho) < n:
        melhor_custo = float('inf')
        melhor_cidade = -1
        melhor_posicao = -1
        
        for cidade in range(n):
            if cidade in visitados:
                continue
            
            for i in range(len(caminho)):
                j = (i + 1) % len(caminho)
                custo = matriz[caminho[i]][cidade] + matriz[cidade][caminho[j]] - matriz[caminho[i]][caminho[j]]
                
                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_cidade = cidade
                    melhor_posicao = j
        
        caminho.insert(melhor_posicao, melhor_cidade)
        visitados.add(melhor_cidade)
    
    return caminho

def calcular_custo(caminho, matriz):
    custo = sum(matriz[caminho[i]][caminho[(i + 1) % len(caminho)]] for i in range(len(caminho)))
    return custo

def medir_tempo_execucao(tamanhos):
    for n in tamanhos:
        matriz = gerar_matriz_adjacencia(n)
        
        inicio = time.time()
        caminho = inserir_mais_barata(matriz)
        fim = time.time()
        
        tempo_execucao = fim - inicio
        print(f"\nInstância com {n} cidades:")
        print(f"Tempo de execução: {tempo_execucao:.5f} segundos")


tamanhos = [4, 6, 8, 10, 12, 14, 16, 18, 20]
medir_tempo_execucao(tamanhos)
