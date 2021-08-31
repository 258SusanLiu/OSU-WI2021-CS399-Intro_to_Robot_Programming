from BirdBrain import Finch
import time

#def checkpoint():
 #   s = finch.getCompass()%9
#    finch.setTurn('L',90-s,50)
 #   print(" ", s)
def moveRight():
    finch.print("R")
    #l,r
    #finch.setMotors(50,0)
    finch.setTurn('R',90,50)
def moveLeft():
    finch.print("L")
    #finch.setMotors(0,50)
    finch.setTurn('L',180,50)
def moveBack():
    finch.print("B")
    #finch.setMotors(0,50)
    finch.setTurn('R',90,50)
    finch.setMove('B',2,50)  
    finch.setTurn('L',180,50)  

def check():
        
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



finch = Finch()

#s = finch.getCompass()%9
#d = 90-s
#finch.setTurn('L',s,50)
#print(" ", s)
#print("d ", d)
#cardboard is (0,0), anything else is light
print("dark",finch.getLight('R'), finch.getLight('L'))
print("Direction ", finch.getDistance())

finch.print("On my Way!")
time.sleep(8)
while finch.getLight('R')<= 3:
    check()
    
finch.stop()
finch.print("Delivered!")


