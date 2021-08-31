from BirdBrain import Finch
import time
import random

#the users 4 choices up, down, left and right

def choice(yn):
    #move left or move right or shake
    c = random.randint(0,3) 
    if c == 0:
        print("Tilt beak up\n")
        #tilt beak up
        time.sleep(5)
        if yn==0 and finch.getOrientation() == 'Beak up':
            #yay
            print("Correct choice\n")
            return int(yn)
        elif yn==1 and finch.getOrientation() == 'Beak up': 
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay
            print("Correct choice\n")
            return int(yn)
        else:
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
    elif c == 1:
        #tilt beak down
        print("Tilt beak down")
        time.sleep(5)
        if yn==0 and finch.getOrientation() == 'Beak down':
            #yay
            print("Correct choice\n")
            return int(yn)
        elif yn==1 and finch.getOrientation() == 'Beak down': 
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay
            print("Correct choice\n")
            return int(yn)
        else:
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
    elif c == 2:
        #tils right
        print("Tilt right")
        time.sleep(5)
        if yn==0 and finch.getOrientation() == 'Tilt right':
            #yay
            print("Correct choice\n")
            return int(yn)
        elif yn==1 and finch.getOrientation() == 'Tilt right': 
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay
            print("Correct choice\n")
            return int(yn)
        else:
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
    elif c == 3:
        #tils left
        print("Tilt left")
        time.sleep(5)
        if yn==0 and finch.getOrientation() == 'Tilt left':
            #yay
            print("Correct choice\n")
            return int(yn)
        elif yn==1 and finch.getOrientation() == 'Tilt left': 
            #no
            print("You lost\n")
            yn = 2
            return int(yn)
        elif yn==1 and finch.getOrientation() != 'Beak up':
            #yay
            print("Correct choice\n")
            return int(yn)
        else:
            #no
            print("You lost\n")
            yn = 2
            return int(yn)

finch = Finch()

stillplaying = 0

stillplaying = int(input("Do You want to play? 1 Yes or 2 no? \n"))
if stillplaying != 1 and stillplaying != 2:
    print("Try again.")

while stillplaying != 2:
    r = random.randint(0,1)
    if r == 0:
        print("Simon Says")
        stillplaying = choice(r)
    elif  r == 1:
        #dont do1
        stillplaying = choice(r)

print("Thank you for playing Simon Says!")