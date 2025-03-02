import numpy as np
import time
import ast
import os

def ler_matrizes_de_arquivos(caminho_pasta):
    """Lê as matrizes de arquivos separados em uma pasta e retorna um dicionário com os nomes dos arquivos e suas matrizes"""
    matrizes = {}
    arquivos = sorted(os.scandir(caminho_pasta), key=lambda x: x.name)  
    
    for arquivo in arquivos:
        if arquivo.is_file():  
            with open(arquivo.path, "r") as f:
                matriz = ast.literal_eval(f.read().strip())
                matrizes[arquivo.name] = matriz
    return matrizes

def vizinho_mais_proximo_tsp(matriz_distancias):
    """Algoritmo do Vizinho Mais Próximo"""
    n = len(matriz_distancias)
    visitado = [False] * n
    caminho = [0] 
    visitado[0] = True
    
    for _ in range(n - 1):
        ultima_cidade = caminho[-1]
        cidade_mais_proxima = None
        menor_distancia = float('inf')
        
        for cidade in range(n):
            if not visitado[cidade] and 0 < matriz_distancias[ultima_cidade][cidade] < menor_distancia:
                menor_distancia = matriz_distancias[ultima_cidade][cidade]
                cidade_mais_proxima = cidade
        
        caminho.append(cidade_mais_proxima)
        visitado[cidade_mais_proxima] = True
    
    caminho.append(0) 
    return caminho

def medir_tempo_execucao(matrizes, iteracoes=9):
    """Mede o tempo médio de execução do algoritmo para cada matriz"""
    resultados = {}
    for nome_arquivo, matriz in matrizes.items():
        tempo_total = 0
        for _ in range(iteracoes):
            tempo_inicio = time.perf_counter()
            vizinho_mais_proximo_tsp(matriz)
            tempo_fim = time.perf_counter()
            tempo_total += (tempo_fim - tempo_inicio)
        resultados[nome_arquivo] = tempo_total / iteracoes
    return resultados

caminho_pasta = "matrizes"
matrizes = ler_matrizes_de_arquivos(caminho_pasta)
resultados = medir_tempo_execucao(matrizes)
for nome_arquivo, tempo_medio in resultados.items():
    print(f"{nome_arquivo}: Tempo médio: {tempo_medio:.10f} segundos")
