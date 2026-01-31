import pgzrun
import random
WIDTH=600
HEIGHT=600
centerx=WIDTH/2
centery=HEIGHT/2
center=(centerx,centery)

Items =["bag","b","waterbottle"]
items =[]
animations =[]
levels = 7
startspeed = 10
gameover = False
gamecomplete = False
currentlevel =1


def draw():
    global items,currentlevel,gameover,gamecomplete 
    screen.clear()
    screen.blit("C:\\Users\\samga\\game development!\\images\\r.jpg",(0,0))
    if gameover:
        displaymessage("GAME OVER!")
    elif gamecomplete:
        displaymessage("YOU WON!")
    else:
        for i in items:
           i.draw()

def update():
    global items
    if len(items)==0:
        items = makeitems(currentlevel)



def makeitems(extraitems):
    itemstocreate= optiontocreate(extraitems)
    newitems = createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems

def optiontocreate(extraitems):
    itemstocreate=["p"]
    for i in range(0,extraitems):
        randomoption=random.choice(Items)
        itemstocreate.append(randomoption)
    return itemstocreate

def createitems(itemstocreate):
    newitems=[]
    #i stand for all items
    for i in itemstocreate:
        item=Actor(i)
        newitems.append(item)
    return newitems

def layoutitems(itemstolayout):
    gaps=len(itemstolayout)+1
    gaps_size=WIDTH/gaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):
        newxpos=(i+1)*gaps_size
        j.x=newxpos

def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=handlegameover,y=HEIGHT)
        animations.append(animation)

def handlegameover():
    global gameover
    gameover=True

def handlegamecomplete():
    global currentlevel,items,animations,gamecomplete
    stopanimation(animations)
    if currentlevel==levels:
        gamecomplete=True
    else:
        currentlevel +=1
        items=[]
        animations=[]

def stopanimation(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()
    
def on_mouse_down(pos):
    global items,currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "p" in i.image:
                handlegamecomplete()
            else:
                handlegameover()

def displaymessage(text1):
    screen.draw.text(text1,fontsize=25,center=center,color="green")

pgzrun.go()



