import pgzrun
import random

WIDTH=800
HEIGHT=600

speed=15
enemies=[]
bullets=[]
score = 0


cat = Actor("C:\\Users\\samga\\game development!\\images\\nyan.png")
cat.pos=(WIDTH//2,HEIGHT-60)
enemies.append(Actor("C:\\Users\\samga\\game development!\\images\\rocket.png"))
enemies[-1].x=10
enemies[-1].y=-100
def draw():
    screen.clear()
    screen.fill("blue")
    for i in bullets:
        i.draw()
    for j in enemies:
        j.draw()    
    cat.draw()
    sd()


def sd():
    screen.draw.text(str(score),(20,20))
    
def on_key_down(key):
    if key==keys.E:
        bullets.append(Actor("C:\\Users\\samga\\game development!\\images\\bullet.png"))
        bullets[-1].x=cat.x
        bullets[-1].y=cat.y-50

def update():
    global score
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
        
    for j in enemies:
        j.y+=5
        if j.y>=HEIGHT:
            j.y=-100
            j.x=random.randint(50,WIDTH-50)    
        for o in bullets:
            if j.colliderect(o):
                score+=5
                bullets.remove(o)    
                enemies.remove(j)

    


pgzrun.go()
