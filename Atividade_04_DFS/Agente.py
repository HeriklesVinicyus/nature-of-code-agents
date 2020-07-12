class Agente:
    def __init__(self, i, j):
        #posicao atual no grid
        self.i = i
        self.j = j
        self.nodes_fechados = []
        self.nodes_abertos = []
    
    def buscar(self):
        pass
        
    def __ver_conexoes_node(self, array_nodes_visiveis):
        '''
        array_nodes_visiveis = nodos visiveis do node atual
        '''
        for x in array_nodes_visiveis:
            if (x not in self.nodes_fechados) or (x not in self.nodes_abertos):
                self.nodes_abertos.append(x)
    
    
        
    
    
