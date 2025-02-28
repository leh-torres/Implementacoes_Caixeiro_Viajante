import sys
from functools import lru_cache
import time

def caixeiroViajante(distancias):
    numCidades = len(distancias)

    @lru_cache(None)
    def menorCaminho(visitadas, ultimaCidade):
        if visitadas == (1 << numCidades) - 1:
            return distancias[ultimaCidade][0], [ultimaCidade]

        melhorCusto = sys.maxsize
        melhorCaminho = []

        for proxima in range(numCidades):
            if (visitadas >> proxima) & 1 == 0:
                novoCusto, caminho = menorCaminho(visitadas | (1 << proxima), proxima)
                novoCusto += distancias[ultimaCidade][proxima]

                if novoCusto < melhorCusto:
                    melhorCusto = novoCusto
                    melhorCaminho = [ultimaCidade] + caminho

        return melhorCusto, melhorCaminho

    inicio = time.time()  
    custo, caminho = menorCaminho(1, 0)
    caminho.append(0)
    fim = time.time() 

    tempo_gasto = fim - inicio
    return custo, caminho, tempo_gasto

# Matriz 
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

custo, caminho, tempo_gasto = caixeiroViajante(distancias)
print(f"Distância mínima: {custo}")
print(f"Melhor caminho: {caminho}")
print(f"Tempo: {tempo_gasto}")
