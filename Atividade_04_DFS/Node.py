class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.valor = 0
        self.nodes_visiveis = []
        self.father = None
        self.g = 0

    def reset(self):
        self.valor = 0

    def mudar_valor(self, valor):
        self.valor = valor

    def set_Father(self, father):
        self.father = father

    def add_array_nodes_visiveis(self, array_nodes):
        for x in array_nodes:
            self.nodes_visiveis.append(x)

    def __str__(self):
        return '[{},{}]'.format(self.i, self.j,)
