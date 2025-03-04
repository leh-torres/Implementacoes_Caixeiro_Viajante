import sys
from functools import lru_cache
import time
import os
import ast

def caixeiroViajante(distancias):
    """Resolve o problema do caixeiro viajante usando programação dinâmica"""
    numCidades = len(distancias)

    @lru_cache(None)
    def menorCaminho(visitadas, ultimaCidade):
        # Caso base: todas as cidades foram visitadas, retornar à cidade inicial
        if visitadas == (1 << numCidades) - 1:
            return distancias[ultimaCidade][0], [ultimaCidade]

        melhorCusto = sys.maxsize
        melhorCaminho = []

        # Tenta visitar cada cidade não visitada
        for proxima in range(numCidades):
            if (visitadas >> proxima) & 1 == 0:
                novoCusto, caminho = menorCaminho(visitadas | (1 << proxima), proxima)
                novoCusto += distancias[ultimaCidade][proxima]

                if novoCusto < melhorCusto:
                    melhorCusto = novoCusto
                    melhorCaminho = [ultimaCidade] + caminho

        return melhorCusto, melhorCaminho

    # Inicia na cidade 0 com apenas ela marcada como visitada (bit 0 = 1)
    custo, caminho = menorCaminho(1, 0)
    caminho.append(0)  # Retorna à cidade inicial para completar o ciclo
    
    return custo, caminho

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
        dist_min, melhor_cam = caixeiroViajante(matriz)
        fim = time.perf_counter()
        
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
        melhores_caminhos.append(melhor_cam)
        menores_distancias.append(dist_min)
        
        print(f"    Distância mínima: {dist_min}")
        print(f"    Melhor caminho: {melhor_cam}")
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
            # Escrever o tempo médio do algoritmo de programação dinâmica
            f.write(f'tempo_medio_pd: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_pd = {tempos}\n')
            f.write(f'        melhor_cam_pd = {melhores_caminhos}\n')
            f.write(f'        menor_dist_pd = {menores_distancias}\n')
    else:
        # Se o arquivo não existir, criar um novo
        with open(nome_resultado, 'w') as f:
            f.write(f'tempo_medio_pd: {tempo_medio:.6f}\n')
            
            # Escrever os arrays de resultados
            f.write(f'        tempos_pd = {tempos}\n')
            f.write(f'        melhor_cam_pd = {melhores_caminhos}\n')
            f.write(f'        menor_dist_pd = {menores_distancias}\n')
    
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