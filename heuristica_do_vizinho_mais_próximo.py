import numpy as np
import time
import ast
import os

def vizinho_mais_proximo_tsp(matriz_distancias):
    """Algoritmo do Vizinho Mais Próximo para o TSP"""
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
    
    caminho.append(0)  # Retorna à cidade inicial
    return caminho

def calcular_custo(caminho, matriz):
    """Calcula o custo total de um caminho"""
    custo = sum(matriz[caminho[i]][caminho[i+1]] for i in range(len(caminho)-1))
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
        caminho = vizinho_mais_proximo_tsp(matriz)
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
            # Escrever o tempo médio do algoritmo de vizinho mais próximo
            f.write(f'tempo_medio_vizinho: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_vizinho = {tempos}\n')
            f.write(f'        melhor_cam_vizinho = {melhores_caminhos}\n')
            f.write(f'        menor_dist_vizinho = {menores_distancias}\n')
    else:
        # Se o arquivo não existir, criar um novo
        with open(nome_resultado, 'w') as f:
            f.write(f'tempo_medio_vizinho: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_vizinho = {tempos}\n')
            f.write(f'        melhor_cam_vizinho = {melhores_caminhos}\n')
            f.write(f'        menor_dist_vizinho = {menores_distancias}\n')
    
    print(f"Resultados salvos em {nome_resultado}")
    
    return tempo_medio

# Exemplo de uso para o arquivo 'matriz4.txt'
if __name__ == "__main__":
    arquivo_matrizes = 'matrizes/matriz4.txt'
    
    # Verificar se o arquivo existe
    if os.path.exists(arquivo_matrizes):
        tempo_medio = processar_arquivo_matrizes(arquivo_matrizes)
    else:
        print(f"Arquivo {arquivo_matrizes} não encontrado!")