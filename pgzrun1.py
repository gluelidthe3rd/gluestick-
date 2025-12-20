import pgzrun
import random

WIDTH =593.119
HEIGHT = 641.284

Ghost = Actor("C:\\Users\\samga\\game development!\\images\\redd.png")

def draw ():
    screen.blit("C:\\Users\\samga\\game development!\\images\\bg.png",(0,0))
    Ghost.draw()

def update ():
    if keyboard.left:
        Ghost.x-=10
    if keyboard.right:
        Ghost.x+=10
    if keyboard.up:
        Ghost.y-=10
    if keyboard.down:
        Ghost.y+=10

def placement():
    Ghost.x=(random.randint(1,599))
    Ghost.y=(random.randint(1,599))
def on_mouse_down(pos):
    if Ghost.collidepoint(pos):
      placement()


pgzrun.go()