import pgzrun
from time import time 
import random

WIDTH = 600
HIEGHT = 600

starttime=0
endtime=0
totaltime=0

Butterflys = []
lines = []
next_bf = 0
nubf = 10
def create_bf():
    global starttime
    for i in range(nubf):
        butterfly = Actor("C:\\Users\\samga\\game development!\\images\\butterfly.png")
        butterfly.pos = random.randint(70,WIDTH-70),random.randint(70,HIEGHT-70)
        Butterflys.append(butterfly)
    starttime = time()
def draw():
    global totaltime
    screen.blit("C:\\Users\\samga\\game development!\\images\\sky.webp",(0,0))
    number=1
    for gi in Butterflys:
        screen.draw.text(str(number),(gi.pos[0],gi.pos[1]+20))
        gi.draw()
        number+=1
    for ki in lines:
        screen.draw.line(ki[0],ki[1],"yellow")
    if next_bf<nubf:
        totaltime = time()-starttime
        screen.draw.text(str(round(totaltime,2)),(60,60),color="black")
    else:
        screen.draw.text(str(round(totaltime,2)),(60,60),color="black")
def update():
    pass
def on_mouse_down(pos):
    global next_bf,lines
    if next_bf <nubf:
        if Butterflys[next_bf].collidepoint(pos):
            if next_bf:
                lines.append((Butterflys[next_bf-1].pos,Butterflys[next_bf].pos))
            next_bf+=1
        else:
            lines=[]
            next_bf=0


create_bf()
pgzrun.go()