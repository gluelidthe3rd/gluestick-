import pgzrun
import random


score=0

WIDTH = 600
HEIGHT = 600
Bee = Actor("C:\\Users\\samga\\game development!\\images\\bee.png")
Bee.pos=300,300
Flower = Actor("C:\\Users\\samga\\game development!\\images\\flower.png")
Flower.pos = 450,450
def draw():
    screen.blit("C:\\Users\\samga\\game development!\\images\\grass.jpg",(0,0))
    Bee.draw()
    Flower.draw()
    screen.draw.text("score: "+ str(score), color="black",topleft =(10,15))

gameover = False
def time():
    global gameover
    gameover= True



def update ():
    global score
    if keyboard.left:
        Bee.x-=10
    if keyboard.right:
        Bee.x+=10
    if keyboard.up:
        Bee.y-=10
    if keyboard.down:
        Bee.y+=10
    FlowerC=Bee.colliderect(Flower)
    if FlowerC:
        ra()
        score+=5

def ra():
    Flower.x=random.randint(10,590)
    Flower.y=random.randint(10,590)
    
clock.schedule(time,60.0)
pgzrun.go()
