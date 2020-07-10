from Nodo import Nodo
import math
import random

class Grid():
    def __init__(self, altura, largura, quant_hor, quant_ver):
        self.altura = altura
        self.largura = largura
        self.quant_hor = quant_hor
        self.quant_ver = quant_ver
        self.nodes = []
        #Bloco de codigo para inicializar a matrix de nodos
        temp_y = 0
        for i in range(0,quant_hor):
            self.nodes.append([])
            temp_x = 0
            lado = largura/quant_hor
            for j in range(0,quant_ver):
                self.nodes[i].append(Nodo(temp_x, temp_y, lado))
                temp_x += lado
            temp_y += lado
            
        self.adicionar_obstaculos()
            
    
    def procurar_posicao_vazia(self):
        while(True):
            i = random.randrange(1, self.quant_hor)
            j = random.randrange(1, self.quant_ver)
            if(self.nodes[i][j].valor == 0):
                return [i,j]
            
    def adicionar_obstaculos(self):
        for i in range(int((self.quant_hor * self.quant_ver)*0.3)):
            aux = self.procurar_posicao_vazia()
            self.nodes[aux[0]][aux[1]].mudar_valor(-1)

    def posicao_agente(self,i,j):
        print(self.nodes[i][j])
        print(i,j)
        self.nodes[i][j].mudar_valor(1)
    
    def add_comida_nodo(self,i, j):
        self.nodes[i][j].mudar_valor(2)
    
    def nodos_visiveis(self, i, j):
        aux = []
        #verifica se tem no a direita
        if(j+1 < self.quant_ver):
            aux.append([i,j+1])
        #verifica se tem no a cima
        if(i-1 > -1 ):
            aux.append([i-1,j])
        #verifica se tem no a baixo
        if(i+1 > self.quant_hor):
            aux.append([i+1,j])
        #verifica se tem no a esqueda
        if(j-1 > -1):
            aux.append([i,j-1])
        
        return aux
        
            
    def display(self):
        for i in self.nodes:
            for j in i:
                j.display()
    
        

            

                        
