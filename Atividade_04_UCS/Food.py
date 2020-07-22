# The "Food" class

class Food():
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.is_dead = False

    def dead(self):
        self.is_dead = True
