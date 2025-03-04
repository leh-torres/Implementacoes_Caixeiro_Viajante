import numpy as np
import random
import time
import os
import ast

def encontrar_menor_aresta(matriz):
    """Encontra a aresta de menor custo na matriz de distâncias"""
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
    """Implementa o algoritmo de inserção mais barata para o TSP"""
    n = len(matriz)
    visitados = set()
    caminho = []
    
    # Inicia com a menor aresta
    u, v = encontrar_menor_aresta(matriz)
    caminho.extend([u, v])
    visitados.update([u, v])
    
    # Adiciona as demais cidades uma a uma
    while len(caminho) < n:
        melhor_custo = float('inf')
        melhor_cidade = -1
        melhor_posicao = -1
        
        for cidade in range(n):
            if cidade in visitados:
                continue
            
            for i in range(len(caminho)):
                j = (i + 1) % len(caminho)
                # Custo de inserir a cidade entre i e j
                custo = matriz[caminho[i]][cidade] + matriz[cidade][caminho[j]] - matriz[caminho[i]][caminho[j]]
                
                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_cidade = cidade
                    melhor_posicao = j
        
        caminho.insert(melhor_posicao, melhor_cidade)
        visitados.add(melhor_cidade)
    
    return caminho

def calcular_custo(caminho, matriz):
    """Calcula o custo total de um caminho"""
    custo = sum(matriz[caminho[i]][caminho[(i + 1) % len(caminho)]] for i in range(len(caminho)))
    return custo

def ler_matrizes_de_arquivo(caminho_arquivo):
    """Lê múltiplas matrizes de um único arquivo, onde cada linha contém uma matriz"""
    matrizes = []
    
    with open(caminho_arquivo, "r") as f:
        for linha in f:
            if linha.strip():  # Ignora linhas vazias
                matriz = ast.literal_eval(linha.strip())
                matrizes.append(matriz)
    
    return matrizes

def processar_arquivo_matrizes(caminho_arquivo):
    # Extrair tamanho da matriz do nome do arquivo
    nome_arquivo = os.path.basename(caminho_arquivo)
    tamanho = nome_arquivo.replace("matriz", "").replace(".txt", "")
    
    # Ler as matrizes do arquivo
    matrizes = ler_matrizes_de_arquivo(caminho_arquivo)
    
    tempos = []
    melhores_caminhos = []
    menores_distancias = []
    
    print(f"Processando {len(matrizes)} matrizes de tamanho {tamanho}...")
    
    # Processar cada matriz
    for i, matriz in enumerate(matrizes):
        print(f"  Processando matriz {i+1}/{len(matrizes)}")
        
        inicio = time.perf_counter()
        caminho = inserir_mais_barata(matriz)
        dist = calcular_custo(caminho, matriz)
        fim = time.perf_counter()
        
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        melhores_caminhos.append(caminho)
        menores_distancias.append(dist)
        
        print(f"    Distância: {dist}")
        print(f"    Caminho: {caminho}")
        print(f"    Tempo de execução: {tempo_execucao:.5f} segundos")
    
    # Calcular tempo médio
    tempo_medio = sum(tempos) / len(tempos)
    print(f"Tempo médio de execução: {tempo_medio:.5f} segundos")
    
    # Criar diretório de resultados se não existir
    os.makedirs('resultados', exist_ok=True)
    
    # Salvar resultado em arquivo
    nome_resultado = f'resultados/tam{tamanho}.txt'
    
    # Verificar se o arquivo já existe e adicionar as informações sem sobrepor
    if os.path.exists(nome_resultado):
        with open(nome_resultado, 'a') as f:
            # Adicionar uma linha em branco para separar
            f.write('\n')
            # Escrever o tempo médio do algoritmo de inserção mais barata
            f.write(f'Tempo Medio Insercao Mais Barata: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_insercao = {tempos}\n')
            f.write(f'        melhor_cam_insercao = {melhores_caminhos}\n')
            f.write(f'        menor_dist_insercao = {menores_distancias}\n')
    else:
        # Se o arquivo não existir, criar um novo
        with open(nome_resultado, 'w') as f:
            f.write(f'Tempo Medio Insercao Mais Barata: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_insercao = {tempos}\n')
            f.write(f'        melhor_cam_insercao = {melhores_caminhos}\n')
            f.write(f'        menor_dist_insercao = {menores_distancias}\n')
    
    print(f"Resultados salvos em {nome_resultado}")
    
    return tempo_medio

# Exemplo de uso para o arquivo 'matriz4.txt'
if __name__ == "__main__":
    arquivo_matrizes = 'matrizes/matriz20.txt'
    
    # Verificar se o arquivo existe
    if os.path.exists(arquivo_matrizes):
        tempo_medio = processar_arquivo_matrizes(arquivo_matrizes)
    else:
        print(f"Arquivo {arquivo_matrizes} não encontrado!")