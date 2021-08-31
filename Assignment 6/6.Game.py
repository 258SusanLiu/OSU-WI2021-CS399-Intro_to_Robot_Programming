from BirdBrain import Finch
from playsound import playsound
import time
import random


#the users 4 choices up, down, left and right

stillplaying = 0
r = 0
def choice(yn):
    global stillplaying
    #move left or move right or shake
    c = random.randint(0,6)
    
    if c == 0:
        finch.setBeak(0, 100, 0)
        playsound('Tiltbeakup.mp3')
        #print("Tilt beak up\n")
        #tilt beak up
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Beak up':
            #yayprint("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Beak up': 
            #noprint("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yayprint("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 1:
        #tilt beak down
        finch.setBeak(0, 100, 0)
        playsound('Tiltbeakdown.mp3')
        #print("Tilt beak down")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Beak down':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Beak down': 
            #noprint("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #noprint("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 2:
        #tils right
        finch.setBeak(0, 100, 0)
        playsound('Tiltright.mp3')
        #print("Tilt right")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Tilt right':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Tilt right': 
            #no print("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 3:
        finch.setBeak(0, 100, 0)
        #tils left
        playsound('Tiltleft.mp3')
        #print("Tilt left")
        time.sleep(3)
        finch.setBeak(100, 0, 0)
        if yn==0 and finch.getOrientation() == 'Tilt left':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() == 'Tilt left': 
            #no print("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay print("Correct choice\n")
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 4:
        #shake
        finch.setBeak(0, 100, 0)
        playsound('shakeme.mp3')
        time.sleep(3)
        if yn==0 and finch.isShaking() == True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.isShaking() == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.isShaking() != True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 5:
        #press A
        finch.setBeak(0, 100, 0)
        playsound('pressbuttona.mp3')
        time.sleep(3)
        if yn==0 and finch.getButton('A')==True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('A') == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('A') != True:
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
    
    elif c == 6:
        #press A
        finch.setBeak(0, 100, 0)
        playsound('pressbuttonb.mp3')
        time.sleep(3)
        if yn==0 and finch.getButton('B')==True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('B') == True: 
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)
        elif yn==1 and finch.getButton('B') != True:
            #yay print("Correct choice\n")
            finch.setBeak(100, 0, 0)
            playsound('correctchoiceaddonepoint.mp3')
            
            stillplaying += 1
            return int(stillplaying)
        else:
            #no print("You lost\n")
            finch.setBeak(100, 0, 0)
            playsound('wrongchoicelooseonepoint.mp3')
            
            stillplaying -= 1
            return int(stillplaying)

def checkWinLose():
    if stillplaying == 10:
        playsound('youwin.mp3')
        #print("Thank you for playing Simon Says!")
        playsound('Thankyouforplaying.mp3')
        playAgain()
    
    elif stillplaying == -1:
        playsound('youloose.mp3')
        playsound('Thankyouforplaying.mp3')
        playAgain()

def points(x):
    if x == -1:
        playsound('1gpoint.mp3')
    elif -1 < x <= 10:
        string = str(x) + 'point.mp3'
        playsound(string)

def playing():
    while stillplaying != 10 and stillplaying != -1:
        global r
        r = random.randint(0,100)

        if r <= 55:
            playsound('Simonsays.mp3')
            choice(0)
            points(stillplaying)
        
        elif  r > 55:
            choice(1)
            points(stillplaying)

def playAgain():
    playsound('input.mp3')
    x = input("")
    
    if x == 'Yes' or x == 'yes':
        global stillplaying
        stillplaying = 0
        again()
    
    if x == 'No' or x == 'no':
        playsound('goodbye.mp3')
        exit

def again():
    playing()

    finch.stopAll()
    checkWinLose()


finch = Finch()

playsound('welcometosimonsays.mp3')
playsound('rules.mp3')

again()