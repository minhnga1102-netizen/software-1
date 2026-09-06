# a function returns random dice (1,6)
import random

def roll_dice():
    return random.randint(1,6)

#main program print result
result = roll_dice()
print(result)

#until result =6
while result != 6:
    result = roll_dice()
    print(result)