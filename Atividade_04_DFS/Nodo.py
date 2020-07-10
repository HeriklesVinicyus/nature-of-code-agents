class Nodo:
    def __init__(self, x,y ,lado):
        self.x = x
        self.y = y
        self.lado = lado
        self.valor = 0
    
    def mudar_valor(self, valor):
        self.valor = valor
        
    def display(self):
        #valor indica que tem parede
        if(self.valor == -1):
            fill(0)
            
        #valor indica que estah vazio
        elif(self.valor == 0):
            fill(255)
            
        #valor indica estah o agente
        elif(self.valor == 1):
            fill(0,255,0)
            
        #valor indica que tem comida
        elif(self.valor == 2):
            fill(255,0,0)
            
        #valor indica que noh fechado
        elif(self.valor == 4):
            fill(128,0,128)
            
        #valor indica que noh aberto
        elif(self.valor == 3):
            fill(0,255,255)
        square(self.x, self.y,self.lado)
            
            
    def __str__(self):
        return 'x = {}, y = {}, valor = {}'.format(self.x,self.y, self.valor)
