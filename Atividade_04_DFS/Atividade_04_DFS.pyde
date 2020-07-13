from Grid import Grid 
from Food import Food
from Agente import Agente

import math

#conf tela
altura = 600
largura = 600
quant_hor = 5#colocar igual a ver(erro serah concertado)
quant_ver = 5#colocar igual a hor(erro serah concertado)
altura_tela = int(math.ceil(altura/quant_ver)*quant_ver)
largura_tela = int(math.ceil(largura/quant_hor)*quant_hor+50)

def setup():    
    global g, f, a

    g = Grid(altura,largura,quant_hor,quant_ver)
     
    aux = g.procurar_posicao_vazia()
    f = Food(aux[0],aux[1])
    
    #configurado para agente iniciar no meio do grid
    a = Agente(int(math.ceil(quant_hor/2)),int(math.ceil(quant_ver/2)))
        
    #Muda a velocidade de que atualiza draw
    frameRate(2)
    
    size(altura_tela, largura_tela)
    background(255)
    
def draw():
    global f
    
    #variavel temporaria para auxiliar a funcao de busca do alimento;
    aux_node = g.retornar_node(a.atual[0], a.atual[1])
    a.buscar_comida(aux_node[0], aux_node[1])
    if (a.achou_comida): 
        f.dead()
        print('b. comida')
        
    if(f.is_dead):
        aux = g.procurar_posicao_vazia()
        f = Food(aux[0],aux[1])
        g.posicao_comida_node(f.i,f.j)
        a.achou_comida = False
        print('a. comida')
    
    g.pintar_nodes_fechados(a.nodes_fechados)
    g.pintar_nodes_abertos(a.nodes_abertos)
    g.posicao_comida_node(f.i,f.j)
    g.posicao_agente(a.i,a.j)

    g.display()
    
    print(g)
