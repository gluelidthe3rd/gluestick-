import pgzrun
import random

WIDTH=800
HEIGHT=600

speed=10
enemies=[]
bullets=[]
score = 0



cat = Actor("C:\\Users\\samga\\game development!\\images\\nyan.png")
cat.pos=(WIDTH//2,HEIGHT-60)
for i in range(7):
    for j in range(2):
        enemies.append(Actor("C:\\Users\\samga\\game development!\\images\\rocket.png"))
        enemies[-1].x=100+50*i
        enemies[-1].y=80+50*j
cat.dead=False
cat.countdown=90

direction=1

def draw():
    screen.clear()
    screen.fill("blue")
    for i in bullets:
        i.draw()
    for j in enemies:
        j.draw() 
    if cat.dead == False:  
        cat.draw()
    sd()
    if len(enemies)==0:
        gameover()

def gameover():
    screen.draw.text("gameover !! you lost",(400,300))
def sd():
    screen.draw.text(str(score),(20,20))
    
def on_key_down(key):
    if cat.dead == False:
        if key==keys.E:
            bullets.append(Actor("C:\\Users\\samga\\game development!\\images\\bullet.png"))
            bullets[-1].x=cat.x
            bullets[-1].y=cat.y-50

def update():
    global score,direction
    movedown=False
    if cat.dead == False:
        if keyboard.a:
            cat.x-=speed
            if cat.x<=0:
                cat.x=0
        elif keyboard.d:
            cat.x+=speed
            if cat.x>=WIDTH:
                cat.x=WIDTH
    for i in bullets:
        if i.y <=0:
            bullets.remove(i)
        else:
            i.y-=10
    if len(enemies)==0:
        gameover()
    if len(enemies)>0 and (enemies[-1].x>WIDTH-80 or enemies[0].x<80):
        movedown = True
        direction = direction*-1
    for j in enemies:
        j.x+=5*direction
        if movedown==True:
            j.y+=100
        if j.y>HEIGHT:
            enemies.remove(j)
        for o in bullets:
            if j.colliderect(o):
                sounds.eep.play()
                score+=5
                bullets.remove(o)    
                enemies.remove(j)
                if len(enemies)==0:
                    gameover()
        if j.colliderect(cat):
            cat.dead=True
    if cat.dead:
        cat.countdown-=1
    if cat.countdown ==0:
        cat.dead=False
        cat.countdown=90
pgzrun.go()
