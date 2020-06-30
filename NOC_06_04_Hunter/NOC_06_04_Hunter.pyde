# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from random import randint
from Vehicle import Vehicle
from Food import Food

def setup():
    global food, vehicle
    size(640, 360)
    food = Food(random(width),random(height), PVector(0,0))
    vehicle = Vehicle(width / 2, height / 2, PVector(0, 0))

def draw():
    background(255)

    #pontuação
    textSize(25)
    text('Pontos {}'.format(vehicle.hunted), 10, 30)
    fill(0, 0, 0)

    global food

    if food.is_dead:
        food = Food(random(width),random(height), PVector(0,0))

    vehicle.hunt(food)
    vehicle.display_food(food)
    vehicle.update()
    vehicle.display()
