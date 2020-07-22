class Agente:
    def __init__(self, nodo_inicial, pontos=0):
        self.pontos = pontos
        # posicao atual no grid
        self.i = nodo_inicial.i
        self.j = nodo_inicial.j

        self.achou_comida = False

        self.nodes_fechados = []
        self.nodes_abertos = [nodo_inicial]
        self.atual = nodo_inicial
        self.dead_lock = False

    # algoritmo de busca
    def buscar_comida(self, food):
        '''
        array_nodes_visiveis = nodos visiveis do node atual
        '''
        # verifica se no node tem comida(valor 2)
        if(self.atual.valor == 2):
            self.i = self.atual.i
            self.j = self.atual.j
            self.__limpar_fechados_aberto()
            self.achou_comida = True
            return self.achou_comida

        for childNode in self.atual.nodes_visiveis:
            if(childNode.valor != -1 and childNode not in self.nodes_fechados) and (childNode not in self.nodes_abertos):
                childNode.set_Father(self.atual)
                childNode.calculate_F(self.atual.g + 1, food.i, food.j)
                self.nodes_abertos.append(childNode)

        self.nodes_fechados.append(self.atual)

        def get_F(node):
            return node.f

        def get_G(node):
            return node.g

        if len(self.nodes_abertos) > 0:
            self.nodes_abertos.sort(key=get_G)
            self.nodes_abertos.sort(key=get_F)

            self.atual = self.nodes_abertos.pop(0)
        else:
            self.dead_lock = True

        return self.achou_comida

    # Rotinas >>
    def __caminhar_ate_comida(self):
        pass

    def __limpar_fechados_aberto(self):
        self.nodes_fechados = []
        self.nodes_abertos = [self.atual]
        self.atual = self.atual
    # <<
