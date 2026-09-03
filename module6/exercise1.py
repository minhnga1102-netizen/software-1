import random
rolls = int(input ("How many dice to roll: "))

sum = 0

for i in range(rolls): 
    roll = random.randint(1,6)
    sum += roll

#dont use while loop here as we know already how many rounds!
# count = 0
# while count <= rolls:
#     number = random.randint(1,6)
#     sum += number
#     count += 1

print(f"Sum of the dice: {sum}")