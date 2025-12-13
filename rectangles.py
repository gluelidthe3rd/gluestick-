import pgzrun
import random

WIDTH= 500
HEIGHT=500

def draw():
    w = 300
    h = 150
    for i in range(15):
        R = Rect((0,0),(w,h))
        R.center = (250,250)
        r = random.randint(120,255)
        g = 0
        b = 255
        screen.draw.rect(R,(r,g,b))
        w-=10
        h+=10
        r-=25
    
pgzrun.go()
