import pygame
import sys
import time
import math
import random

WIDTH = 500
HEIGHT = 500
rt2 = math.sqrt(2)

square_x = WIDTH / 2 - HEIGHT /2
square_y = 0
square_side = HEIGHT

circle_x = (WIDTH/2)
circle_y = (HEIGHT/2)
cirlce_rad = HEIGHT / 2

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

pt = []
in_circle_count = 0
in_square_count = 0
pi = 0

x = 30
y = 30
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

#collect initial position and length of square as parameters
def put_point_in_square ():
    x = random.uniform(WIDTH / 2 - HEIGHT / 2 , WIDTH / 2 + HEIGHT / 2)
    y = random.uniform(0 , HEIGHT)
    return (x,y)

def distance (a,b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]
    dist = math.sqrt(delta_x**2 + delta_y**2)
    return dist

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen,RED,(square_x ,square_y, square_side,square_side),3)
pygame.draw.circle(screen,BLUE,(int(circle_x),int(circle_y)),int(cirlce_rad),3)
pygame.display.update()

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT ):
            sys.exit()
        if (event.type == pygame.KEYDOWN ):
            if(event.key == pygame.K_ESCAPE):
                sys.exit()

    temp = put_point_in_square()
    pt.append(temp)

    in_square_count += 1
    if(distance((circle_x,circle_y),temp) <= cirlce_rad):
        in_circle_count += 1

    screen.fill(WHITE,(temp,(2,2)))
    pygame.display.update()
    time.sleep(0.01)


    try:
        pi = 4 * in_circle_count / in_square_count
        print("circle = " + str(in_circle_count) + " square = " + str(in_square_count))
        print("pi = " + str(pi))
        print(math.pi)
    except ZeroDivisionError:
        print("circle = " + str(in_circle_count) + " square = " + str(in_square_count))
        print("pi = " + "infinity")
