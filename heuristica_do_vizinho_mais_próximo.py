import numpy as np
import time

def gerar_matriz_distancia(n, seed=None):
    if seed:
        np.random.seed(seed)
    matriz = np.random.randint(10, 100, size=(n, n))
    np.fill_diagonal(matriz, 0)  
    return matriz

def vizinho_mais_proximo_tsp(matriz_distancia):
    n = len(matriz_distancia)
    visitadas = [False] * n
    caminho = [0] 
    visitadas[0] = True
    
    for _ in range(n - 1):
        ultima_cidade = caminho[-1]
        cidade_proxima = None
        menor_distancia = float('inf')
        
        for cidade in range(n):
            if not visitadas[cidade] and 0 < matriz_distancia[ultima_cidade][cidade] < menor_distancia:
                menor_distancia = matriz_distancia[ultima_cidade][cidade]
                cidade_proxima = cidade
        
        caminho.append(cidade_proxima)
        visitadas[cidade_proxima] = True
    
    caminho.append(0)  
    return caminho

def medir_tempo_execucao(n, iteracoes=10):
    tempo_total = 0
    for _ in range(iteracoes):
        matriz = gerar_matriz_distancia(n)
        inicio_tempo = time.perf_counter()
        vizinho_mais_proximo_tsp(matriz)
        fim_tempo = time.perf_counter()
        tempo_total += (fim_tempo - inicio_tempo)
    return tempo_total / iteracoes

tamanhos = [4, 6, 8, 10, 12, 14, 16, 18, 20]
resultados = {n: medir_tempo_execucao(n) for n in tamanhos}

for n, tempo_medio in resultados.items():
    print(f"Cidades: {n}, Tempo médio: {tempo_medio:.6f} segundos")
