from Node import Node
import math
import random


class Grid():
    def __init__(self, altura, largura, quant_hor, quant_ver):
        self.altura = altura
        self.largura = largura
        # x
        self.quant_hor = quant_hor
        # y
        self.quant_ver = quant_ver

        self.nodes = []

        # Rotina de inicializacao
        self.__iniciar_matrix_nodes()
        self.__adicionar_obstaculos()
        self.__adicionar_nodes_visiveis()

    def posicao_agente(self, i, j):
        self.nodes[i][j].mudar_valor(1)

    def posicao_comida_node(self, i, j):
        self.nodes[i][j].mudar_valor(2)

    def pintar_nodes_fechados(self, array_fechados):  # TUDO Mudar para nome melhor
        for x in array_fechados:
            self.nodes[x.i][x.j].mudar_valor(4)

    def pintar_nodes_abertos(self, array_abertos):  # TUDO Mudar para nome melhor
        for x in array_abertos:
            self.nodes[x.i][x.j].mudar_valor(3)

    def pintar_nodes_atual(self, atual):  # TUDO Mudar para nome melhor
        self.nodes[atual.i][atual.j].mudar_valor(5)

    # TUDO Mudar para nome melhor
    def pintar_proximo_node_anilizado(self, prox):
        self.nodes[prox.i][prox.j].mudar_valor(6)

    def procurar_posicao_vazia(self):
        self.__limpar_fechados_abertos_comida()
        while(True):
            i = random.randrange(0, self.quant_ver)
            j = random.randrange(0, self.quant_hor)
            if(self.nodes[i][j].valor == 0 and i != int(math.ceil(self.quant_hor/2)) and j != int(math.ceil(self.quant_ver/2))):
                return [i, j]

    # Rotinas de inicializacao>>
    def __iniciar_matrix_nodes(self):

        for i in range(self.quant_ver):
            aux = []
            for j in range(self.quant_hor):
                aux.append(Node(i, j))
            self.nodes.append(aux)

    def __adicionar_obstaculos(self):
        for i in range(int((self.quant_hor * self.quant_ver)*0.2)):
            aux = self.procurar_posicao_vazia()
            self.nodes[aux[0]][aux[1]].mudar_valor(-1)

    # Dentro do node existe uma variavel com os nodes que ela conhece. essa funcao adiciona os valores dos nodes visiveis
    def __adicionar_nodes_visiveis(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                aux = []
                # verifica se tem no a direita
                if(j+1 < self.quant_hor and self.nodes[i][j+1].valor != -1):
                    aux.append(self.nodes[i][j+1])
                # verifica se tem no a cima
                if(i-1 > -1 and self.nodes[i-1][j].valor != -1):
                    aux.append(self.nodes[i-1][j])
                # verifica se tem no a esqueda
                if(j-1 > -1 and self.nodes[i][j-1].valor != -1):
                    aux.append(self.nodes[i][j-1])
                # verifica se tem no a baixo
                if(i+1 < self.quant_ver and self.nodes[i+1][j].valor != -1):
                    aux.append(self.nodes[i+1][j])

                self.nodes[i][j].add_array_nodes_visiveis(aux)

    def __limpar_fechados_abertos_comida(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i])):
                if (self.nodes[i][j].valor in [1, 2, 3, 4, 5, 6]):
                    self.nodes[i][j].mudar_valor(0)
    # Rotinas<<

    def display(self, run=False):
        aux_altura = math.ceil(self.altura/self.quant_ver)
        aux_largura = math.ceil(self.largura/self.quant_hor)
        aux_y = 0
        for i in self.nodes:
            aux_x = 0
            for j in i:
                # valor indica que tem parede (Preto)
                if(j.valor == -1):
                    fill(0)

                # valor indica que estah vazio (Branco)
                elif(j.valor == 0):
                    fill(255)

                # valor indica onde estah o agente (Verde)
                elif(j.valor == 1):
                    fill(0, 200, 0)

                # valor indica que tem comida (Vermelha)
                elif(j.valor == 2):
                    fill(200, 0, 0)

                elif(run == True):
                    fill(255)

                # valor indica que noh fechado (Roxo)
                elif(j.valor == 4 and run == False):
                    fill(128, 0, 128)

                # valor indica que noh aberto (Ciano)
                elif(j.valor == 3 and run == False):
                    fill(0, 255, 255)

                # valor indica qual serah o proximo noh
                elif(j.valor == 5 and run == False):
                    fill(243, 156, 18)

                # valor indica qual eh o noh atual de observado
                elif(j.valor == 6 and run == False):
                    fill(3, 155, 229)

                rect(aux_x, aux_y, aux_largura, aux_altura)
                aux_x += aux_largura
            aux_y += aux_altura
    #

    def __str__(self):
        aux = ''
        for x in self.nodes:
            for y in x:
                aux += '{:>3}'.format(y.valor)
            aux += '\n'
        return aux
