from BirdBrain import Finch
from datetime import datetime
from playsound import playsound
import random
from Games import *
import time, random, threading


#check where the parameters came from and choose the right option for the event
def check(wherefrom,num):
    if wherefrom == "water":
        time.sleep(20)
        #print("Can I also have a sip of water? Tilt my beak down to give me a sip of water")
        playsound('ProgramSound/water1.mp3')
        time.sleep(5)
        finch.setBeak(100,0,0)
        if num == 1 or num == 2 or num == 3 or num == 4 and finch.getOrientation() == 'Beak down':
            playsound('ProgramSound/water2.mp3')
        time.sleep(5)

    elif wherefrom == "food":
        if num == 1:
            #print("Have you had breakfast?")print("if you have please press A, if you havent press B")
            playsound('ProgramSound/breakfastyn.mp3')
            playsound('ProgramSound/pressb.mp3')
            finch.setBeak(0,100,0)
            while finch.getButton('A')== False and finch.getButton('b')==False:
                time.sleep(1)
            
            finch.setBeak(100,0,0)
            if finch.getButton('A'):
                #print("Great! Lets eat a snack!")
                playsound('ProgramSound/letseatsnacks.mp3')
                time.sleep(20)
                #print("Can I have a bite too? Tip my beak down please")
                playsound('ProgramSound/canihaveabite.mp3')
                while finch.getOrientation() != 'Beak down':
                    #print("Thanks for giving me a bite!")
                    finch.setBeak(0,100,0)
                    time.sleep(1)
                finch.setBeak(100,0,0)
                playsound('ProgramSound/thanksforbite.mp3')
            elif finch.getButton('B'):
                #finch.setBeak(0,100,0)
                #print("Oh no! Let go make some breakfast! Lets make scrambled eggs, bacon and toast\n")print("You will need eggs, bacon, bread, butter, salt and pepper")print("Press A if you have all the ingrediant, press B if you're getting the ingrediants")
                playsound('ProgramSound/breakfast1.mp3')
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    #wait
                    time.sleep(1)
                    finch.setBeak(0,100,0)
             
                finch.setBeak(100,0,0)
                #print("Now that you have all your ingrediants lets start making our food!")print("Lets cook the bacon! Place the bacon in the pan and cook.")print("Press button A when done")
                playsound('ProgramSound/breakfast2.mp3')
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now lets cook the scrambled eggs.")print("Lets crack the eggs in the bowl and scramble the eggs then add some salt and pepper and cook in pan.")print("Press button A when done")
                playsound('ProgramSound/breakfast3.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now lets cook some toast!")print("Let's take the bread and butter both sides and cook one side in pan until golden colored and flip and cook till the other side is golden colored.")print("Press button A when done")
                playsound('ProgramSound/breakfast4.mp3')
                finch.setBeak(0,100,0)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                finch.stopAll()
                #print("Lets go eat!")
                playsound('ProgramSound/letsgoeat.mp3')
                time.sleep(10)
                
                while finch.getOrientation() != 'Beak down':
                    #print("Can I have a bite too? Tip my beak down please")
                    finch.setBeak(0,100,0)
                    playsound('ProgramSound/canihaveabite.mp3')
                    time.sleep(10)
                time.sleep(1)
                finch.setBeak(100,0,0)
                if finch.getOrientation() == 'Beak down':
                    #print("Thanks for giving me a bite!")
                    playsound('ProgramSound/thanksforbite.mp3')

        elif num == 2:
            playsound('ProgramSound/lunchyn.mp3')
            playsound('ProgramSound/pressb.mp3')
            finch.setBeak(0,100,0)
            while finch.getButton('A')== False and finch.getButton('b')==False:
                time.sleep(1)
            
            finch.setBeak(100,0,0)
            if finch.getButton('A'):
                #print("Great! Lets eat a snack!")
                playsound('ProgramSound/letseatsnacks.mp3')
                time.sleep(20)
                #print("Can I have a bite too? Tip my beak down please")
                playsound('ProgramSound/canihaveabite.mp3')
                while finch.getOrientation() != 'Beak down':
                    #print("Thanks for giving me a bite!")
                    finch.setBeak(0,100,0)
                    time.sleep(1)
                finch.setBeak(100,0,0)
                playsound('ProgramSound/thanksforbite.mp3')
            elif finch.getButton('B'):
                #print("Oh no! Let go make some lunch! Lets make a Caesar wrap\n")print("You will need Caesar salad dressing, grated Parmesan, garlic powder, pepper, cooked chicken breast, romaine lettece, croutons and wheat tortillas")print("Press A if you have all the ingrediant, press B if you're getting the ingrediants")
                playsound('ProgramSound/lunch1.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now that you have all your ingrediants lets start making our food!")print("Lets make the filling. Put lettece, croutons, paresan, garlic powder, pepper and chicken breast in a bowl. Then mix and add in the caesar salad dressing and mix again.")print("Press button A when done")
                playsound('ProgramSound/lunch2.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now lets grab a wheat tortilla and fill it with the mixture. Then wrap up the mixture to make the ceasar wrap")print("Press button A when done")
                playsound('ProgramSound/lunch3.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                finch.stopAll()
                playsound('ProgramSound/letsgoeat.mp3')
                time.sleep(10)
                
                while finch.getOrientation() != 'Beak down':
                    #print("Can I have a bite too? Tip my beak down please")
                    playsound('ProgramSound/canihaveabite.mp3')
                    finch.setBeak(0,100,0)
                    time.sleep(10)
                time.sleep(1)
                finch.setBeak(100,0,0)
                if finch.getOrientation() == 'Beak down':
                    #print("Thanks for giving me a bite!")
                    playsound('ProgramSound/thanksforbite.mp3')

        elif num == 3:
            playsound('ProgramSound/dinneryn.mp3')
            playsound('ProgramSound/pressb.mp3')
            finch.setBeak(0,100,0)
            if finch.getButton('A'):
                finch.setBeak(100,0,0)
                playsound('ProgramSound/letseatsnacks.mp3')
                time.sleep(20)
                playsound('ProgramSound/canihaveabite.mp3')
                while finch.getOrientation() != 'Beak down':
                    #print("Thanks for giving me a bite!")
                    finch.setBeak(0,100,0)
                    time.sleep(1)
                finch.setBeak(100,0,0)
                playsound('ProgramSound/thanksforbite.mp3')
            elif finch.getButton('B'):
                #print("Oh no! Let go make some dinner. Lets make shrimp scampi!\n")print("You will need noodles, butter, olive oil, dry white wine, red pepper flakes, shrimp, parsley, garlic, and lemon juice")print("Press A if you have all the ingrediant, press B if you're getting the ingrediants")

                playsound('ProgramSound/dinner1.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now that you have all your ingrediants lets start making our food!")print("Lets make the sauce to cook the shrimp in. In a pan melt butter with olive oil over medium heat, then add garlic and saute until fragrant.")print("Press button A when done")
                playsound('ProgramSound/dinner2.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now lets add wine and bring to a simmer, once wine reduce by half add salt, pepper flakes and black pepper.")print("Press button A when done")
                playsound('ProgramSound/dinner3.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Add in shrimp and saute until shrimp is pink. Stir in parsley and lemon juice.")print("Press button A when done")
                playsound('ProgramSound/dinner4.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Now take the shrimp and butter pan and put it on the side. Now, lets cook the noodles in the water")print("Press button A when done")
                playsound('ProgramSound/dinner5.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Take a few spoonfuls of noodle water and pour it into the shrimp and butter pan, stir, and toss the noodles in!")print("Press button A when done")
                playsound('ProgramSound/dinner6.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                #print("Lets put everything onto a plate and you're done!")print("Press button A when done")
                playsound('ProgramSound/dinner7.mp3')
                finch.setBeak(0,100,0)
                finch.stopAll()
                finch.setBeak(0,100,0)
                time.sleep(3)
                while not finch.getButton('A'):
                    finch.setBeak(0,100,0)
                    #wait
                    time.sleep(1)
                finch.setBeak(100,0,0)
                finch.stopAll()
                playsound('ProgramSound/letsgoeat.mp3')
                finch.setBeak(0,100,0)
                time.sleep(10)
                
                while finch.getOrientation() != 'Beak down':
                    playsound('ProgramSound/canihaveabite.mp3')
                    time.sleep(10)
                time.sleep(1)
                finch.setBeak(100,0,0)
                if finch.getOrientation() == 'Beak down':
                    playsound('ProgramSound/thanksforbite.mp3')
        
        elif num == 4:
            #playsound('ProgramSound/letseatsnacks.mp3')
            time.sleep(20)
            playsound('ProgramSound/canihaveabite.mp3')
            finch.setBeak(0,100,0)
            time.sleep(1)
            if finch.getOrientation() == 'Beak down':
                playsound('ProgramSound/thanksforbite.mp3')  
                finch.setBeak(100,0,0)    

            time.sleep(5)
    
    elif wherefrom == "exercise":
        s=0
        if num == 1:
            #print("Walk forward and backward 5 times holding the finch")
            playsound('ProgramSound/walkholdingfinch.mp3')
            time.sleep(5)
            while s != 5:
                print(s)
                x = finch.getDistance()
                
                time.sleep(10)
                if x > finch.getDistance():
                    s += 1
                    #sound and red light
                    finch.setBeak(100,0,0)
                    finch.playNote(100,1)
                    #print("Please turn around")
                    playsound('ProgramSound/turnaround.mp3')
                    time.sleep(5)
                    #green light
                    finch.setBeak(0,100,0)
                else:
                    #print("I was not able to sense that time, please walk again")
                    playsound('ProgramSound/walkredo.mp3')
                    finch.setBeak(0,100,0)
            #print("Thanks for doing a light exercise with me!")
            playsound('ProgramSound/thankslightexercise.mp3')
            finch.stopAll()
        
        elif num == 2:
            #Leg exercise
            time.sleep(5)
            #print("lets do 10 squats")
            playsound('ProgramSound/do10squats.mp3')
            time.sleep(2)
            finch.setBeak(0,100,0)
            while s != 10:
                #print(s+1, " squat")
                ss= str(s+1)+'squat.mp3'
                playsound('ProgramSound/'+ss)
                time.sleep(3)
                s+=1
            s=0
            
            finch.setBeak(100,0,0)
            time.sleep(2)
            finch.setBeak(0,100,0)
            #print("Lets do 10 lunges")
            playsound('ProgramSound/do10lunges.mp3')
            time.sleep(2)
            while s != 10:
                #print(s+1, " lunge")
                ss= str(s+1)+'lunge.mp3'
                playsound('ProgramSound/'+ss)
                time.sleep(4)
                s+=1
            #print("Thanks for doing some leg exercies with me!")
            finch.setBeak(100,0,0)
            playsound('ProgramSound/thankslegexercise.mp3')
            time.sleep(5)
        
        elif num == 3:
            #print("lets do 10 pushups")
            playsound('ProgramSound/do10pushups.mp3')
            time.sleep(5)
            finch.setBeak(0,100,0)
            while s != 10:
                #print(s+1, " pushup")
                ss= str(s+1)+'pushup.mp3'
                playsound('ProgramSound/'+ss)
                time.sleep(4)
                s+=1
            s=0
            finch.setBeak(100,0,0)
            time.sleep(1)
            #print("Lets do a 30 second plank")
            playsound('ProgramSound/30secplank.mp3')
            finch.setBeak(0,100,0)
            while s!=30:
                print(s+1, " second")
                time.sleep(1)
                s+=1
            finch.setBeak(100,0,0)
            #print("Thanks for doing some upper body exercies with me!")
            playsound('ProgramSound/thanksupperbodyexercise.mp3')

        elif num == 4:
            #print("Lets do the right quad stretch for 15 seconds")
            playsound('ProgramSound/rightquad15sec.mp3')
            finch.setBeak(0,100,0)
            while s!=15:
                print(s+1, " second")
                time.sleep(1)
                s+=1
            finch.setBeak(100,0,0)
            s=0
            time.sleep(1)
            #print("Lets do the left quad stretch for 15 seconds")
            playsound('ProgramSound/leftquad15sec.mp3')
            finch.setBeak(0,100,0)
            while s!=15:
                print(s+1, " second")
                time.sleep(1)
                s+=1
            finch.setBeak(100,0,0)
            s=0
            time.sleep(1)
            #print("Lets  do butterfly for 20 seconds")
            playsound('ProgramSound/butterfly20sec.mp3')
            finch.setBeak(0,100,0)
            while s!=20:
                print(s+1, " second")
                time.sleep(1)
                s+=1
            finch.setBeak(100,0,0)
            time.sleep(1)
            #print("Thanks for stretching with me!")
            playsound('ProgramSound/thanksstretching.mp3')
    
    elif wherefrom == "play":
        if num == 1:
            #print("Simon Says")
            playsound('ProgramSound/playsimonsays.mp3')
            time.sleep(1)
            finch.setBeak(0,100,0)
            SimonSays()
            finch.setBeak(100,0,0)
        
        elif num == 2:
            #print("Please give me something to draw with")
            playsound('ProgramSound/drawsomething.mp3')
            time.sleep(10)
            finch.setBeak(0,100,0)
            draw()
            finch.setBeak(100,0,0)
        
        elif num == 3:
            #print("Maze")
            playsound('ProgramSound/maze.mp3')
            time.sleep(10)
            finch.setBeak(0,100,0)
            Maze()
            finch.setBeak(100,0,0)
        time.sleep(5)
    
#image of Mr.Octopus jumping up and down and spinning to get user attention  
def jump():
    finch.setBeak(100,0,0)
    finch.setDisplay([0,0,0,0,0,
                     0,1,1,1,0,
                     1,1,0,1,1,
                     0,1,1,1,0,
                     1,0,1,0,1])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                    1,1,0,1,1,
                    0,1,1,1,0,
                    1,0,1,0,1,
                    0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                     0,1,1,1,0,
                     1,1,0,1,1,
                     0,1,1,1,0,
                     1,0,1,0,1])
    time.sleep(1)
    finch.setMotors(-1,1)
    finch.setTurn('L',360,100)
    finch.setBeak(0,100,0)

#image of Mr.Octopus sinking down and sleeping
def sleep():
    finch.setBeak(100,0,0)
    finch.setDisplay([0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1,
                      0,1,1,1,0,
                      1,0,1,0,1])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,1,0,
                      0,0,0,0,0,
                      0,0,0,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,1,
                      0,0,0,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,1,0,
                      0,0,0,0,0,
                      0,0,0,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,1,
                      0,0,0,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,1,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,1,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0])
    
    x = random.randint(1,30)    #120
    time.sleep(x)

    finch.setTurn('L',45,80)
    finch.setTurn('R',90,80)
    finch.setTurn('L',45,80)
    finch.setBeak(0,100,0)
    time.sleep(2)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1,
                      0,1,1,1,0])
    time.sleep(1)                      
    finch.setDisplay([0,0,0,0,0,
                      0,1,1,1,0,
                      1,1,0,1,1,
                      0,1,1,1,0,
                      1,0,1,0,1])

#interactive symbol water cup being filled and emptied
#check time of day and choose option for water
def water():
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0])    
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0])    
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,0,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
    finch.setDisplay([0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0,
                      0,1,1,1,0])
    time.sleep(1)
def ynwater():
    finch.setBeak(0,100,0)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print("I have eaten my snack, have you eaten your snack?  ", current_time)
    if "08:00" < current_time < "13:00":
        #print("Make Sure to drink some liquids with your breakfast")
        playsound('ProgramSound/waterbreakfast.mp3')
        check("water",1)
    elif "13:00" < current_time < "18:00":
        #print("Make sure to drink some water with lunch")
        playsound('ProgramSound/waterlunch.mp3')
        check("water",2)
    elif "18:00" < current_time < "23:00":
        #print("Make sure to drink something during dinner~")
        playsound('ProgramSound/waterdinner.mp3')
        check("water",3)
    else:
        #print("Please drink some water")
        check("water",4)

#interactive symbol chicken wing being eaten
#check time of day and choose option for food
def food():
    finch.setDisplay([0,0,0,1,0,
                      0,1,0,1,1,
                      1,0,1,0,0,
                      1,0,0,1,0,
                      0,1,1,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,1,0,
                      0,1,0,1,1,
                      1,0,1,0,0,
                      1,0,1,0,0,
                      0,1,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,1,0,
                      0,1,0,1,1,
                      1,0,1,0,0,
                      1,1,0,0,0,
                      0,1,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,1,0,
                      0,1,0,1,1,
                      1,0,1,0,0,
                      0,1,0,0,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,1,0,
                      0,0,0,1,1,
                      0,0,1,0,0,
                      0,1,0,0,0,
                      0,0,0,0,0])
    time.sleep(1) 
def ynfood():  
    finch.setBeak(0,100,0)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print("I have eaten my snack, have you eaten your snack?  ", current_time)
    if "08:00" < current_time < "10:00":
        #print("Make Sure to eat breakfast")
        playsound('ProgramSound/letseatbreakfast.mp3')
        check("food",1)
    elif "11:00" < current_time < "13:00":
        #print("Make sure to eat lunch")
        playsound('ProgramSound/letseatlunch.mp3')
        check("food",2)
    elif "17:00" < current_time < "20:00":
        #print("Make sure to eat dinner~")
        playsound('ProgramSound/letseatdinner.mp3')
        check("food",3)
    else:
        #print("Please eat a snack")
        playsound('ProgramSound/letseatsnacks.mp3')
        check("food",4)

#interactive symbol dumbell moving up and down
#check time of day and choose option for exercise
def exercise():
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,1,0,1,0,
                      1,1,1,1,1,
                      0,1,0,1,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,1,0,1,0,
                      1,1,1,1,1,
                      0,1,0,1,0,
                      0,0,0,0,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,1,0,1,0,
                      1,1,1,1,1,
                      0,1,0,1,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,1,0,1,0,
                      1,1,1,1,1,
                      0,1,0,1,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,1,0,1,0,
                      1,1,1,1,1,
                      0,1,0,1,0,
                      0,0,0,0,0])
    time.sleep(1)
def ynexercise():
    finch.setBeak(0,100,0)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #print("I have eaten my snack, have you eaten your snack?  ", current_time)
    if "08:00" < current_time < "12:00":
        #print("Lets do some light exercises")
        playsound('ProgramSound/lightexercise.mp3')
        check("exercise",1)
    elif "13:00" < current_time < "17:00":
        #print("Lets do some leg exercises")
        playsound('ProgramSound/legexercise.mp3')
        check("exercise",2)
    elif "18:00" < current_time < "23:00":
        #print("Lets do some upper body exercises")
        playsound('ProgramSound/upperbodyexercise.mp3')
        check("exercise",3)
    else:
        #print("Lets do some stretches")
        playsound('ProgramSound/stretches.mp3')
        check("exercise",4)

#interactive symbol play button
#check time of day and choose option for play
def play():
    finch.setDisplay([0,1,0,0,0,
                      0,1,1,0,0,
                      0,1,1,1,1,
                      0,1,1,0,0,
                      0,1,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,1,1,0,0,
                      0,1,1,1,0,
                      0,1,1,0,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0])
    time.sleep(1)    
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,0,0,0,0,
                      0,0,0,0,0,
                      0,0,1,0,0,
                      0,0,0,0,0,
                      0,0,0,0,0])
    time.sleep(1)  
    finch.setDisplay([0,0,0,0,0,
                      0,1,1,0,0,
                      0,1,1,1,0,
                      0,1,1,0,0,
                      0,0,0,0,0])
    time.sleep(1)
    finch.setDisplay([0,1,0,0,0,
                      0,1,1,0,0,
                      0,1,1,1,1,
                      0,1,1,0,0,
                      0,1,0,0,0])
def ynplay():
    finch.setBeak(0,100,0)
    #print("Lets play")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if "00:00" < current_time < "08:00":
        check("play",1)
    elif "08:00" < current_time < "16:00":
        #print("Lets see what I can Draw")
        playsound('ProgramSound/draw.mp3')
        check("play",2)
    elif "16:00" < current_time < "24:00":
        check("play",3)


def runn():
    x = random.random()
    jump()
    time.sleep(1)
    
    if x <= 0.2:
        #time.sleep(5)
        #print("I'm hungry! Lets go eat a snack")
        finch.setBeak(0,100,0)
        playsound('ProgramSound/letsgoeatsnack.mp3')
        food()
        ynfood()
    
    if .2< x <= .5:
        #time.sleep(10)
        #print("I'm thristy, lets go get some water to drink!")
        finch.setBeak(0,100,0)
        playsound('ProgramSound/letsgetwater.mp3')
        water()
        ynwater()
    
    if .5< x <= .8:
        #time.sleep(15)
        #print('Lets go exercise')
        finch.setBeak(0,100,0)
        playsound('ProgramSound/letsgoexercise.mp3')
        exercise()
        ynexercise()
    
    if .8< x <= 1:
        #time.sleep(20)
        #print('Im bored lets go play')
        finch.setBeak(0,100,0)
        playsound('ProgramSound/letsgoplay.mp3')
        play()
        ynplay()
    sleep()

finch = Finch()

#run the program in a loop until the finch is shaken
#exit loop when finch is shaken and end program
while finch.isShaking() == False:
    runn()
finch.stopAll()
playsound('ProgramSound/bye.mp3')
exit()