class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.valor = 0
        self.nodes_visiveis = []
    
    def mudar_valor(self, valor):
        self.valor = valor
    
    def add_array_nodes_visiveis(self, array_nodes):
        self.nodes_visiveis.append(array_nodes)
    
    def __str__(self):
        return 'i = {}, j = {}, valor = {}, nodes visiveis = {}'.format(self.i,self.j, self.valor, self.nodes_visiveis)
