class Agente:
    def __init__(self,nodo_inicial):
        self.pontos = 0
        #posicao atual no grid
        self.i = nodo_inicial.i
        self.j = nodo_inicial.j
        
        self.achou_comida = False
        self.posicao_comida = []#test
        self.caminho = []#test
        
        self.nodes_fechados = []
        self.nodes_abertos = [nodo_inicial]
        self.atual = nodo_inicial
        
    #algoritmo de busca
    def buscar_comida(self, conteudo, array_nodes_visiveis):
        '''
        array_nodes_visiveis = nodos visiveis do node atual
        '''
        # verifica se no node tem comida(valor 2)
        if(conteudo == 2):
            self.i = self.atual.i
            self.j = self.atual.j
            self.__limpar_fechados_aberto()
            self.achou_comida = True
            self.pontos += 1
            return self.achou_comida
            
        aux_pilha_nodes = array_nodes_visiveis
        for x in aux_pilha_nodes:
            if(x not in self.nodes_fechados) and (x not in self.nodes_abertos):
                self.nodes_abertos.append(x)
                
        self.nodes_fechados.append(self.atual)        
        self.atual = self.nodes_abertos.pop(0) if len(self.nodes_abertos)>0 else self.atual
        
        
        return self.achou_comida
    
    #Rotinas >>
    def __caminhar_ate_comida(self):
        pass
        
    def __limpar_fechados_aberto(self):
        self.nodes_fechados = []
        self.nodes_abertos = [self.atual]
        self.atual = self.atual
    #<<
