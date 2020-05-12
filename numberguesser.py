# Title: Number Guessing Game                                          #
# Aim: Make a program which randomly chooses a number to guess and     #
# then the user will have a few chances to guess the number correctly. #
# In each wrong attempt, the computer will give a hint that the number #
# is greater or smaller than the one you have guessed.                 #

import random
import math

print("""
The aim of this game is to guess the number the computer has picked.
You will have three chances to get the number correct.
Good luck!
""")

int num = random()
int maxNum = input()
