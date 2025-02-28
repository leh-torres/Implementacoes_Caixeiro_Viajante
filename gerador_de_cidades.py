import random

class Gerador_de_Cidades():

    def __init__(self, tamanho):
        self.tam = tamanho
        self.m_pesos = []

    def gerar_matriz_de_adj(self):
        self.m_pesos = [[0]*self.tam for _ in range(self.tam)]

        for i in range(self.tam):
            for j in range(self.tam):

                if i == j:
                    self.m_pesos[i][j] = 0

                if self.m_pesos[j][i] != 0:
                    self.m_pesos[i][j] = self.m_pesos[j][i]

                if i != j and self.m_pesos[i][j] == 0:
                    num_aleatorio = random.randint(0, 50)

                    if num_aleatorio == 0:
                        num_aleatorio = -1
                    else: 
                        pass

                    self.m_pesos[i][j] = num_aleatorio
                
        print(self.m_pesos)

    def salvar_matriz(self):
        nome = 'matriz' + str(self.tam) + '.txt'
        with open(nome, 'w') as arq:
            arq.write(str(self.m_pesos))


if __name__ == '__main__':

    tam = [4, 6, 8, 10, 12, 14, 16, 18, 20]

    for i in tam:
        gerador = Gerador_de_Cidades(i)
        gerador.gerar_matriz_de_adj()
        gerador.salvar_matriz()



    