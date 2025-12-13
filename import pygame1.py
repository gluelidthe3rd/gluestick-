import pygame
import random
pygame.init()
WIDTH= 500
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))

def draw():
    for i in range(15):
        r = random.randint(120,255)
        g = 0
        b = 255
        t = (300,200)
        y =(230,280)
        u =(380,280)
        tri = [t,y,u]
        pygame.draw.polygon(screen,(r,g,b),tri)
        t-=10
        y-=10
        u-=10
        r-=25


