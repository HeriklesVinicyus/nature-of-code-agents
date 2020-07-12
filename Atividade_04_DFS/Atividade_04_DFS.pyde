from Grid import Grid 
from Food import Food
from Agente import Agente

import math

#conf tela
altura = 500
largura = 500
quant_hor = 41
quant_ver = 41
altura_tela = int(math.ceil(altura/quant_ver)*quant_ver)
largura_tela = int(math.ceil(largura/quant_hor)*quant_hor+50)

def setup():
        
    global g, f, a

    g = Grid(altura,largura,quant_hor,quant_ver)
    
    aux = g.procurar_posicao_vazia()
    f = Food(aux[0],aux[1])
    g.posicao_comida_node(f.i,f.j)
    
    a = Agente(int(math.ceil(quant_hor/2)),int(math.ceil(quant_ver/2)))
    
    size(altura_tela, largura_tela)
    background(255)
    frameRate(2)
    
def draw():
    global f
    g.display()
    g.posicao_agente(a.i,a.j)
     
    if(f.is_dead):
        aux = g.procurar_posicao_vazia()
        f = Food(aux[0],aux[1])
        g.posicao_comida_node(f.i,f.j)
