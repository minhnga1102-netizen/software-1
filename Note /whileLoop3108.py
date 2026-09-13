#FIXED amount of repetition: constant value: rounds, expect inp0ut from user
rounds = int (input ("How many greetings: "))

finished_rounds = 0

while finished_rounds < rounds:
    print ("Good morning")
    finished_rounds +=1


#User ends repetition
command = input ("Enter command: ")
while command != 'stop':
    print ("Executing command: " + command)
    command = input ("Enter command: ")
print ("execution stopped.")

# Varying amount of repetition
import random
dice1 = dice2 = rolls = 0
while dice1 != 6 or dice2 != 6:
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    rolls +=1
print (f"Rolled {rolls} times")

#nested loop
first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print (f"{first} times {second} is {first*second}")
        second +=1
    first +=1

# tung 100,000 rounds, moi round tinh so roll can thiet de 66
# tong so roll tung round/ rounds

import random
rounds = 0
total_rolls = 0

while rounds <= 100000:
    dice1 = dice2 = rolls = 0
    while (dice1 != 6 or dice2 != 6):
        dice1 = random.randint (1,6)
        dice2 = random.randint (1,6)
        rolls += 1
    rounds += 1
    total_rolls += rolls

average_rolls = total_rolls/rounds
print (f"Average rolls required: {average_rolls:6.2f}")


#BREAK
command = input ("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print ("Excecuting command: + command")
    command = input ("Enter command: ")
print ("Execution stopped.")

#WHILE/ELSE

command = input ("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print ("Executing command: + command")
    command = input ("Enter command: ")
# this line run only command != mayday, otherwise break immediately
else:
    print ("goodbye")

# this line is outside of loop, always printed after loop ended
print ("execution stopped")



#INFINITE LOOP
number = 1
while number < 5:
    print (number)
    number +=1

print ("ready")