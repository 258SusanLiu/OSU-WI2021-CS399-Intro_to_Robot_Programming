from BirdBrain import Finch
import time

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

def candy(c):
    if c==1:
        #morse code for 'Candy Yes'
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,4)
        time.sleep(1)

        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,2)
        time.sleep(.5)
    elif c==2:
        #morse code for 'Candy No'        
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,2)
        time.sleep(.5)
        
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)
        finch.playNote(85,4)
        time.sleep(1)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,2)
        time.sleep(.5)

        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,4)
        time.sleep(1)
        finch.playNote(85,4)
        time.sleep(1)


finch = Finch()


finch.print("Doyoulikecandy")

time.sleep(10)

finch.print("AisYesBisNo")
time.sleep(8)
finch.stopAll()
if finch.getButton('A')==True:
    finch.setMove('F',1,100)
    finch.setMove('B',1,100)
    finch.setMove('F',1,100)
    finch.setMove('B',1,100)
    finch.print("Candy Yes")
    candy(1)
elif finch.getButton('B')==True:
    finch.setTurn('L',5,100)
    finch.setTurn('R',5,100)
    finch.setTurn('L',5,100)
    finch.setTurn('R',5,100)
    finch.print("Candy No")
    candy(2)

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

finch.print("This is the end!")
