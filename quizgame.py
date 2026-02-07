import pgzrun

TITLE="quiz master"
WIDTH=600
HIEGHT=600

answerbox1=Rect(0,0,250,100)
answerbox2=Rect(0,0,250,100)
answerbox3=Rect(0,0,250,100)
answerbox4=Rect(0,0,250,100)
abl=[answerbox1,answerbox2,answerbox3,answerbox4]
welcomebox=Rect(0,0,565,60)
questionbox=Rect(0,0,530,85)
questionbox.move_ip(30,75)
welcomebox.move_ip(15,5)
answerbox1.move_ip(45,180)
answerbox2.move_ip(300,180)
answerbox3.move_ip(45,320)
answerbox4.move_ip(300,320)
def draw():
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(questionbox,"orange")
    screen.draw.filled_rect(welcomebox,"white")
    for i in abl:
        screen.draw.filled_rect(i,"green")


pgzrun.go()