from Grid import Grid 
from Food import Food
from Agente import Agente

def setup():
    #Cenario
    global g, f, a
    
    g = Grid(500,500,20,20)#não colar valor impar(erro futuramente concertado)
    aux = g.procurar_posicao_vazia()
    f = Food(aux[0],aux[1])
    a = Agente()
    
    size(500,550)
    background(255)
    
    
    
def draw():
      g.display()
      g.posicao_agente(a.i,a.j)

      
