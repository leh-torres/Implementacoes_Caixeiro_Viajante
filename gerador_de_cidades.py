import random
import math
import os

class Gerador_de_Cidades():

    def __init__(self, tamanho):
        self.tam = tamanho
        self.cidades = []
        self.m_pesos = []

    def gerar_pontos(self):
        self.cidades = [] 
        cid_anterior = (0, 0)
        tamanho = self.tam

        while tamanho != 0:
            x = random.randint(1, 40)
            y = random.randint(1, 40)

            cid = (x, y)

            if(cid != cid_anterior):
                self.cidades.append(cid)
                cid_anterior = cid
                tamanho -= 1
        
        # print(self.cidades)  

    def calcula_dist(self, p1, p2):
        return math.sqrt(math.pow((p2[0]-p1[0]), 2) + math.pow((p2[1]-p1[1]), 2))

    def gerar_matriz_de_adj(self):
        self.m_pesos = [[0]*self.tam for _ in range(self.tam)]
        self.gerar_pontos()

        for i in range(self.tam):
            for j in range(self.tam):

                if i == j:
                    self.m_pesos[i][j] = 0

                if self.m_pesos[j][i] != 0:
                    self.m_pesos[i][j] = self.m_pesos[j][i]

                if i != j and self.m_pesos[i][j] == 0:
                    dist = self.calcula_dist(self.cidades[i], self.cidades[j])

                    self.m_pesos[i][j] = dist
                
        # print('Matriz finalizada!')  
        return self.m_pesos

    def salvar_matrizes(matrizes, tamanho):
        
        os.makedirs('matrizes', exist_ok=True)
        
        nome = 'matrizes/matriz' + str(tamanho) + '.txt'
        with open(nome, 'w') as arq:
            for matriz in matrizes:
                arq.write(str(matriz) + '\n')  


if __name__ == '__main__':
    tam = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    for i in tam:
        matrizes = []  
        
        for j in range(10):
            gerador = Gerador_de_Cidades(i)
            matriz = gerador.gerar_matriz_de_adj()
            matrizes.append(matriz)
            print(f"  Matriz {j+1}/10 ")
        
        Gerador_de_Cidades.salvar_matrizes(matrizes, i)