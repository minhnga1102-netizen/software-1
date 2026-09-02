# ran_number+ random.randint(1-10) computer generate random number
# input = guest a number
# input < ran_number -> Too low
# input > ran_number -> Too high
# input == ran_number -> Correct. program ENDS HERE


import random
random_number = random.randint(1,10)

user_input = input("Guess a number: ")
guess = float(user_input)

#loop continues while user enter wrong numbers

while guess != random_number:
    if guess < random_number:
        print ("Too low")
    else:
        print ("Too high")
    user_input = input("Guess a number: ")
    guess = float(user_input)
print ("Correct")