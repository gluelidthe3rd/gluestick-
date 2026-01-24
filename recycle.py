import pgzrun
WIDTH=600
HEIGHT=600
centerx=WIDTH/2
centery=HEIGHT/2
center=(centerx,centery)

Items =["pb","b","pw"]
items =[]
animations =[]

def draw():
    global items 
    screen.clear()
    screen.blit("C:\\Users\\samga\\game development!\\images\\r.jpg",(0,0))
    for i in items:
        i.draw()

def makeitems(extraitems):
    itemstocreate= optiontocreate(extraitems)
    newitems = createitems(itemstocreate)
    layout_items(newitems)
    animateitems(newitems)
    return newitems