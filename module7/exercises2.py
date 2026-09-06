# a function returns random dice (1,6)
#2.parameter: number of sides of dice *user_input
import random

sides = int(input("Enter the number of sides on the dice: "))

def roll_dice(sides):
    return random.randint(1,sides)

#main program print result
result = roll_dice(sides)
print(result)

#until result = sides
while result != sides:
    result = roll_dice(sides)
    print(result)