from BirdBrain import Finch
import time

def moveRight():
    finch.print("R")
    finch.setTurn('R',90,50)
def moveLeft():
    finch.print("L")
    finch.setTurn('L',180,50)  
def moveBack():
    finch.print("B")
    finch.setTurn('L',90,50)  

def check():
    if finch.getDistance() <= 10:
        finch.setMove('B',1,50)
        moveRight()
        if finch.getDistance() <=10:
            finch.setMove('B',1,50)
            moveLeft()
            if finch.getDistance() <=10:
                
                finch.setMove('B',1,50)
                moveBack()
    elif finch.getDistance() >6:
        finch.print("F")
        finch.setMove('F',10,100)



finch = Finch()

while finch.isShaking()!=True:
    check()
        
