# Title: Number Guessing Game                                          #
# Aim: Make a program which randomly chooses a number to guess and     #
# then the user will have a few chances to guess the number correctly. #
# In each wrong attempt, the computer will give a hint that the number #
# is greater or smaller than the one you have guessed.                 #

import random
import pprint
import sys

print("The aim of this game is to guess the number the computer has picked.",
"\n", "You will have three chances to get the number correct.",
"\n", "Good luck!")

maxNum = 10
correctNum = random.randint(1, maxNum)

def playerGuess():
    guessNum = input("Enter your guess: ")
    if guessNum == correctNum:
        print("You have guess correctly. The answer was " + correctNum)
    elif guessNum > correctNum:
        print("Ahaha too high!")
    elif guessNum < correctNum:
        print("Ahaha too small!")

playerGuess()
playerGuess()
playerGuess()
