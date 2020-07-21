# The "Food" class

class Food():

    def __init__(self, x, y, vel):
        self.position = PVector(x, y)
        self.r = 6
        self.is_dead = False

    def display(self):
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
    
    # Funcao para matar o objeto 
    def dead(self):
        self.is_dead = True
