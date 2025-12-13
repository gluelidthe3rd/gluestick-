import pgzrun

WIDTH= 500
HEIGHT=500

r = [(214, 6, 6),(255, 117, 43),(255, 213, 43),(6, 214, 17),(0, 64, 255),(136, 6, 207)]

def draw():
    CAT=100
    for i in range(15):
#r[1%len(r)] will go through all colours and if there are not enought it will repeat
        screen.draw.filled_circle((250,250),CAT,r[i%len(r)])
        CAT-=5
    
pgzrun.go()