class Grid():
    # A cell object knows about its location in the grid 
    # it also knows of its size with the variables x,y,w,h.
    def __init__(self, varX, varY, varW, varH):
        self.x = varX
        self.y = varY
        self.w = varW
        self.h = varH
    

    def display(self):
        #stroke(255)
        fill(255)
        rect(self.x,self.y,self.w,self.h)
        
              

    def draw_grid(nCols, nRows, grid):
        background(0)
        # The counter variables i and j are also the column and row numbers and 
        # are used as arguments to the constructor for each object in the grid.  
        for i in xrange(nCols):
            for j in xrange(nRows):
                # Oscillate and display each object
                grid[i][j].display()
                
                        
