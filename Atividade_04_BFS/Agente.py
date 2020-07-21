class Agente:
    def __init__(self, nodo_inicial, pontos=0):
        self.pontos = pontos
        # posicao atual no grid
        self.i = nodo_inicial.i
        self.j = nodo_inicial.j

        self.achou_comida = False
        self.posicao_comida = []  # test
        self.caminho = []  # test

        self.nodes_fechados = []
        self.nodes_abertos = [nodo_inicial]
        self.atual = nodo_inicial
        self.dead_lock = False

    # algoritmo de busca
    def buscar_comida(self):
        '''
        array_nodes_visiveis = nodos visiveis do node atual
        '''
        # verifica se no node tem comida(valor 2)
        if(self.atual.valor == 2):
            self.i = self.atual.i
            self.j = self.atual.j
            self.__limpar_fechados_aberto()
            self.achou_comida = True
            self.pontos += 1
            return self.achou_comida

        for childNode in self.atual.nodes_visiveis:
            if(childNode.valor != -1 and childNode not in self.nodes_fechados) and (childNode not in self.nodes_abertos):
                childNode.setFather(self.atual)
                self.nodes_abertos.append(childNode)

        self.nodes_fechados.append(self.atual)
        if len(self.nodes_abertos) > 0:
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
