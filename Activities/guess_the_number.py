#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
numofguesses=0
for numofguesses in range(3):
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess) # converts a string to an integer
        numofguesses+=1
        if numofguesses==3:
            print("Game Over")
            break
        if (guess>aRandomNumber):
            print("Try guessing lower!")
        elif (guess<aRandomNumber):
            print("Try guessing higher!")
        else:
            print("Correct!")
            break
        

