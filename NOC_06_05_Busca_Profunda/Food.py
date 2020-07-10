# The "Food" class

class Food():

    def __init__(self, array_ij):
        self.x = array_ij[0]
        self.y = array_ij[1]
        self.is_dead = False
    


    def dead(self):
        self.is_dead = True
