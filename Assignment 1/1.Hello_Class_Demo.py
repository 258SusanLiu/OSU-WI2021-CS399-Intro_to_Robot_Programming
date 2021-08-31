from BirdBrain import Finch
import time


finch = Finch()

finch.stopAll()
finch.stopAll()

finch.setBeak(100,0,0)
finch.stopAll()
finch.setBeak(0,100,0)
finch.stopAll()
finch.setBeak(0,0,100)
finch.stopAll()
finch.stopAll()

#morse code for 'I Like Candy'
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()

finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()

finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()

finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()

finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()

finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,2)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()
finch.playNote(85,4)
finch.stopAll()


#green
finch.setTail(1,50,100,50)
finch.stopAll()
#yellow
finch.setTail(1,100,100,50)
finch.stopAll()
#blue
finch.setTail(1,50,100,100)
finch.stopAll()
#white
finch.setTail(1,100,100,100)
finch.stopAll()

#green
finch.setTail(2,50,100,50)
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



finch.print("Hi my name is Susan!")

finch.setMove('F',5,80)
finch.setTurn('R',36,80)
finch.setMove('F',5,80)
finch.setTurn('L',108,80)
finch.setMove('F',5,80)
finch.setTurn('R',36,80)
finch.setMove('F',5,80)
finch.setTurn('L',108,80)
finch.setMove('F',5,80)
finch.setTurn('R',36,80)
finch.setMove('F',5,80)
finch.setTurn('L',108,80)
finch.setMove('F',5,80)
finch.setTurn('R',36,80)
finch.setMove('F',5,80)
finch.setTurn('L',108,80)
finch.setMove('F',5,80)
finch.setTurn('R',36,80)
finch.setMove('F',5,80)
finch.setTurn('L',108,80)
finch.setMove('F',5,80)

finch.setMove('B',15,100)
finch.print("Wheeeeeeee~")

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

finch.print("This is the end!")
