class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.valor = 0
        self.nodes_visiveis = []
        self.father = None
        self.f = 0
        self.g = 0
        self.h = 0

    def reset(self):
        self.valor = 0
        self.f = 0
        self.g = 0
        self.h = 0

    def calculate_F(self, g, i, j):
        self.g = g
        self.h = abs(self.i - i) + abs(self.j - j)
        self.f = self.h + self.g

    def mudar_valor(self, valor):
        self.valor = valor

    def set_Father(self, father):
        self.father = father

    def add_array_nodes_visiveis(self, array_nodes):
        for x in array_nodes:
            self.nodes_visiveis.append(x)

    def __str__(self):
        return '[{},{}]'.format(self.i, self.j,)
