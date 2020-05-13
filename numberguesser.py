# Title: Number Guessing Game                                          #
# Aim: Make a program which randomly chooses a number to guess and     #
# then the user will have a few chances to guess the number correctly. #
# In each wrong attempt, the computer will give a hint that the number #
# is greater or smaller than the one you have guessed.                 #

import random
import pprint
import sys

print("The aim of this game is to guess the number the computer has picked.",
"\n", "You will have five chances to get the number correct.",
"\n", "Good luck!")

numberFound = False
maxNum = 20
correctNum = random.randint(1, maxNum)
numGuesses = 5

def playerGuess():
    global numberFound
    global numGuesses

    while numberFound == False:
        guessNum = int(input("Enter your guess: "))
        if guessNum == correctNum:
            print("You have guessed correctly. The answer was ", correctNum)
            numberFound = True
        elif guessNum > correctNum:
            print("Ahaha too high!")
            numGuesses -= 1
        elif guessNum < correctNum:
            print("Ahaha too small!")
            numGuesses -= 1
        if numGuesses == 0:
            print("Too bad, you didn't get the correct answer.",
            "\n", "The correct answer was ", correctNum)
            break
        

playerGuess()
