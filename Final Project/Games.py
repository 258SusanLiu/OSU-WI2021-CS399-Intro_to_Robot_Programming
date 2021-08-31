from BirdBrain import Finch
from playsound import playsound
import random
import time



#DRAW GAME
#draw out shapes the finch will move around and drar out a picture
#make sure to put a pen or marker in the finch pen holder
def lights():
    finch.setBeak(100,0,0)
    finch.stopAll()
    finch.setBeak(0,100,0)
    finch.stopAll()
    finch.setBeak(0,0,100)
    finch.stopAll()
    #green
    finch.setTail(1,50,100,50)
    finch.stopAll()
    #yellow
    finch.setTail(1,100,100,500)
    finch.stopAll()
    #blue
    finch.setTail(1,50,100,100)
    finch.stopAll()
    #white
    finch.setTail(1,100,100,10)
    finch.stopAll()

    #green
    finch.setTail(2,50,100,500)
    finch.stopAll()
    #yellow
    finch.setTail(2,100,100,50)
    finch.stopAll()
    #blue
    finch.setTail(2,50,100,100)
    finch.stopAll()
    #white
    finch.setTail(2,100,100,100)
    finch.stopAll()

    #green
    finch.setTail(3,50,100,50)
    finch.stopAll()
    #yellow
    finch.setTail(3,100,100,50)
    finch.stopAll()
    #blue
    finch.setTail(3,50,100,100)
    finch.stopAll()
    #white
    finch.setTail(3,100,100,100)
    finch.stopAll()

    #green
    finch.setTail(4,50,100,50)
    finch.stopAll()
    #yellow
    finch.setTail(4,100,100,50)
    finch.stopAll()
    #blue
    finch.setTail(4,50,100,100)
    finch.stopAll()
    #white
    finch.setTail(4,100,100,100)
    finch.stopAll()

def star(i):
    for x in range(5):
        finch.setMove('F',i,80)
        finch.setTurn('R',36,80)
        finch.setMove('F',i,80)
        finch.setTurn('L',108,80)
    
    finch.setMove('F',i,80)

def draw():
    lights()

    star(5)
    finch.setMove('B',15,100)
    finch.print("Wheeeeeeee~")
    star(2)
    finch.setTurn('L',90,80)
    finch.setMove('F',15,100)

    finch.setTurn('L',108,80)
    finch.setMove('F',15,100)
    finch.setMove('F',15,100)
    finch.setTurn('R',90,80)
    finch.setMove('F',15,100)
    finch.setTurn('R',90,80)
    finch.setMove('F',15,100)
    finch.setTurn('R',90,80)
    finch.setMove('F',15,100)
    finch.setTurn('R',90,80)
    finch.setTurn('R',90,80)
    finch.setMove('F',15,100)
    finch.setTurn('R',135,80)
    finch.setMove('F',22,100)

    lights()



#SIMON SAYS GAME
#preform the event when Simon says 'simon says' and dont preform the event
#if Simon does not say 'simon says'
#the users 4 choices up, down, left and right
stillplaying = 0
rs = 0
def choice(yn):
    global stillplaying
    #move left or move right or shake
    c = random.randint(0,6)
    
    if c == 0:
        finch.setBeak(0, 100, 0)
        playsound('Sounds/Tiltbeakup.mp3')
        #print("Tilt beak up\n")
        #tilt beak up
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Beak up':
            #yayprint("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Beak up': 
            #noprint("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yayprint("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 1:
        #tilt beak down
        finch.setBeak(0, 100, 0)
        playsound('Sounds/Tiltbeakdown.mp3')
        #print("Tilt beak down")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Beak down':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Beak down': 
            #noprint("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #noprint("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 2:
        #tils right
        finch.setBeak(0, 100, 0)
        playsound('Sounds/Tiltright.mp3')
        #print("Tilt right")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Tilt right':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Tilt right': 
            #no print("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 3:
        finch.setBeak(0, 100, 0)
        #tils left
        playsound('Sounds/Tiltleft.mp3')
        #print("Tilt left")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Tilt left':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Tilt left': 
            #no print("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 4:
        #shake
        finch.setBeak(0, 100, 0)
        playsound('Sounds/shakeme.mp3')
        time.sleep(3)
        if yn==0 and finch.isShaking() == True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.isShaking() == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.isShaking() != True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 5:
        #press A
        finch.setBeak(0, 100, 0)
        playsound('Sounds/pressbuttona.mp3')
        time.sleep(3)
        if yn==0 and finch.getButton('A')==True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('A') == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('A') != True:
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 6:
        #press A
        finch.setBeak(0, 100, 0)
        playsound('Sounds/pressbuttonb.mp3')
        time.sleep(3)
        if yn==0 and finch.getButton('B')==True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('B') == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('B') != True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('Sounds/wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)

def checkWinLose():
    if stillplaying == 10:
        playsound('Sounds/youwin.mp3')
        #print("Thank you for playing Simon Says!")
        playsound('Sounds/Thankyouforplaying.mp3')
        playAgain()
    
    elif stillplaying == -1:
        playsound('Sounds/youloose.mp3')
        playsound('Sounds/Thankyouforplaying.mp3')
        playAgain()

def points(x):
    if x == -1:
        playsound('sounds/1gpoint.mp3')
    elif -1 < x <= 10:
        string = 'sounds/' + str(x) + 'point.mp3'
        playsound(string)

def playings():
    while stillplaying != 10 and stillplaying != -1:
        global rs
        rs = random.randrange(100)

        if rs <= 55:
            playsound('Sounds/Simonsays.mp3')
            choice(0)
            points(stillplaying)
        
        elif  rs > 55:
            choice(1)
            points(stillplaying)

def playAgain():
    playsound('sounds/input.mp3')
    x = input("")
    
    if x == 'Yes' or x == 'yes':
        global stillplaying
        stillplaying = 0
        SimonSays()
    
    if x == 'No' or x == 'no':
        playsound('sounds/goodbye.mp3')
        exit

def SimonSays():
    playings()

    finch.stopAll()
    checkWinLose()



#MAZE GAME
#robot will travel through a maze and make turns
#robot moves right
def moveRight():
    finch.print("R")
    #l,r
    #finch.setMotors(50,0)
    finch.setTurn('R',90,50)

#robot moves left
def moveLeft():
    finch.print("L")
    #finch.setMotors(0,50)
    finch.setTurn('L',180,50)

#robot turns around and head the opposite way
def moveBack():
    finch.print("B")
    #finch.setMotors(0,50)
    finch.setTurn('R',90,50)
    finch.setMove('B',2,50)  
    finch.setTurn('L',180,50)  

def check():
    #going forward
    finch.print('F')
    finch.setMotors(50,50)
    d = finch.getDistance()
    finch.setMove('F', d-5,20)

    if finch.getDistance() <= 10:
        finch.setMove('B',1,50)
        moveRight()
        if finch.getDistance() <=10:
            finch.setMove('B',1,50)
            moveLeft()
            if finch.getDistance() <=10:
                finch.setMove('B',1,50)
                moveBack()

def Maze():
    print("dark",finch.getLight('R'), finch.getLight('L'))
    time.sleep(8)

    #checking for light
    while finch.isShaking() != True:
        check()
        
    finch.stop()

finch = Finch()

