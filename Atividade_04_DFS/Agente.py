class Agente:
    def __init__(self, i, j):
        self.pontos = 0
        #posicao atual no grid
        self.i = i
        self.j = j
        
        self.achou_comida = False
        self.posicao_comida = []#test
        self.caminho = []#test
        
        self.nodes_fechados = []
        self.nodes_abertos = [[i,j]]
        self.atual = [i,j]
        #test
        self.caminho = []
    
    def buscar_comida(self, conteudo, array_nodes_visiveis):
        '''
        array_nodes_visiveis = nodos visiveis do node atual
        '''
        # verifica se no node tem comida(valor 2)
        if(conteudo == 2):
            self.i = self.atual[0]
            self.j = self.atual[1]
            self.__limpar_fechados_aberto()
            self.achou_comida = True
            self.pontos += 1
            
            return self.achou_comida
            
        self.atual = self.nodes_abertos.pop(-1) if len(self.nodes_abertos)>0 else self.atual
        
        aux_pilha_nodes = array_nodes_visiveis
        for x in aux_pilha_nodes:
            if(x not in self.nodes_fechados) and (x not in self.nodes_abertos):
                self.nodes_abertos.append(x)
        
        self.nodes_fechados.append(self.atual)
        return self.achou_comida
    
    def __caminhar_ate_comida(self):
        pass
        
    def __limpar_fechados_aberto(self):
        self.nodes_fechados = []
        self.nodes_abertos = [[self.i,self.j]]
        self.atual = [self.i,self.j]
