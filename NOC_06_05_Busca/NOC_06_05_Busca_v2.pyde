from random import randrange
from Vehicle import Vehicle
from Food import Food
            
from Grid import Grid

# w is size of each cell 
w = 10

def setup():
    
    frameRate(10)
    
    #Setup para a construção do gáfico
    global nCols, nRows, grid
    size(640, 360)
    nCols = int(width/w)
    nRows = int(height/w)
    grid = makeGrid()
    for j in xrange(nRows):
        for i in xrange(nCols):
            # Initialize each object
            grid[i][j] = Grid(i*w,j*w,w,w)

    #Setup da Comida e do Veiculo            
    global food, vehicle
    food = Food(randrange(1,width/w+1)*w - w, randrange(1,height/w+1)*w - w, PVector(0,0))
    vehicle = Vehicle((width/(2*w)-1)*w, (height/(2*w)-1)*w, PVector(0, 0), w)
        
def draw():
    
    # Código para construção gáfica do Grid
    global nCols, nRows, grid
    background(10)
    # The counter variables i and j are also the column and row numbers and 
    # are used as arguments to the constructor for each object in the grid.  
    for i in xrange(nCols):
        for j in xrange(nRows):
            # Oscillate and display each object
            grid[i][j].display()

    # Código para construção gáfica da Pontuação
    fill(255)
    if (vehicle.hunted < 10):
        rect(w, 2*w, 13*w, 3*w)
    elif ((vehicle.hunted >= 10) and (vehicle.hunted < 100)):
        rect(w, 2*w, 15*w, 3*w)
    elif ((vehicle.hunted >= 100) and (vehicle.hunted < 1000)):
        rect(w, 2*w, 17*w, 3*w)
    else: rect(w, 2*w, 19*w, 3*w)
        
    fill(0)
    textSize(3*w)
    text('Pontos {}'.format(vehicle.hunted), w, 5*w)
    
    global food
    
    if food.is_dead:
        food = Food(randrange(1,width/w+1)*w - w, randrange(1,height/w+1)*w - w, PVector(0,0))
    
    #vehicle.hunt(food)
    vehicle.hunt_Grid(food)
    vehicle.display_food(food)
    vehicle.update()
    vehicle.display()

# Creates a 2D List of 0's, nCols x nRows large
def makeGrid():
    global nCols, nRows
    grid = []
    for i in xrange(nCols):
        # Create an empty list for each row
        grid.append([])
        for j in xrange(nRows):
            # Pad each column in each row with a 0
            grid[i].append(0)
    return grid
