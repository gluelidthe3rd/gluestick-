import pgzrun

TITLE="quiz master"
WIDTH=600
HIEGHT=600

questionfile="C:\\Users\\samga\\game development!\\questions.txt"
score=0
timeleft=10
msg=""
gameover=False
questions=[]
count=0
index=0

timer=Rect(0,0,80,80)
skipbox=Rect(0,0,400,85)
answerbox1=Rect(0,0,250,100)
answerbox2=Rect(0,0,250,100)
answerbox3=Rect(0,0,250,100)
answerbox4=Rect(0,0,250,100)
abl=[answerbox1,answerbox2,answerbox3,answerbox4]
welcomebox=Rect(0,0,565,60)
questionbox=Rect(0,0,530,85)
questionbox.move_ip(30,75)
skipbox.move_ip(30,450)
timer.move_ip(450,450)
welcomebox.move_ip(15,5)
answerbox1.move_ip(45,180)
answerbox2.move_ip(300,180)
answerbox3.move_ip(45,320)
answerbox4.move_ip(300,320)
def draw():
    global msg
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(questionbox,"orange")
    screen.draw.filled_rect(welcomebox,"white")
    screen.draw.filled_rect(skipbox,"red")
    screen.draw.filled_rect(timer,"blue")
    for i in abl:
        screen.draw.filled_rect(i,"green")
    msg="welcome to the guessing game! get through all the questions to win!"
    msg=msg+f"Q:{index}of{count}"
    screen.draw.textbox(msg,welcomebox,color="black")
    screen.draw.textbox(str(timeleft),timer,color="white")
    screen.draw.textbox(question[0].strip(),questionbox,color="white")
    screen.draw.textbox("click here to skip",skipbox,color="white")
    i=1
    for u in abl:
        screen.draw.textbox(question[i].strip(),u,color="black")
        i+=1
def readquestion():
    global count,questions
    q_file=open(questionfile,"r")
    for i in q_file:
        questions.append(i)
        count+=1
    q_file.close()

def readnextquestion():
    global index
    index+=1
    return questions.pop(0).split(",")
def movemsg():
    welcomebox.x=welcomebox.x-2
    if welcomebox.right <0:
        welcomebox.left=WIDTH
def update():
    movemsg()

def on_mouse_down(pos):
    i =1
    for j in abl:
        if j.collidepoint(pos):
            if i is int(question[5]):
                correct_answer()
            else:
                game_over()
        i+=1
    if skipbox.collidepoint(pos):
        skipquestion()

def correct_answer():
    global score,question,timeleft,questions
    score+=1
    if questions:
        question=readnextquestion()
        timeleft=10
    else:game_over()
def game_over():
    global question,timeleft,gameover
    message =f"GAME OVER! you got {score} questions correct"
    question =[message,"-","-","-","-",5]
    timeleft=0
    gameover=True

def skipquestion():
    global question,timeleft
    if questions and not gameover:
        question=readnextquestion()
        timeleft=10
    else:
        game_over()
        
def updatetimeleft():
    global timeleft
    if timeleft:
        timeleft-=1
    else:
        game_over()

readquestion()
question=readnextquestion()
clock.schedule_interval(updatetimeleft,1)
pgzrun.go()