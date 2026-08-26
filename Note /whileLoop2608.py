rounds = int (input ("How many rounds: "))

finished_rounds = 0

while finished_rounds< rounds:
    print ("greetings!")
    finished_rounds += 1 



counter = 0
while counter < 5:
    print ('hi')
    counter += 2


counter = 5
while counter >=0:
    print (counter)
    counter -=1

outer = 1
while outer <= 5:
    inner = 1
    while inner <= 5:
        product = inner * outer
        print (f"{outer} times {inner} is {product}")
        inner +=1
    outer +=1


#create a calculator program. 
# The calculator allow user to make calculations until they quit
# print a menu : + - *
# ask user 2 numbers 
# finally, print result 
# then, print menu again, allow user choose new calculation + 2 new nums

menu_list = "Select option:\n1.add\n2.minus\n3.multiple\n0.exit"
user_choice = input(menu_list)


while user_choice != "EXIT":

    num1 = float (input ('Please enter number 1: '))
    num2 = float (input ('Please enter number 2: '))

    if user_choice == '1': 
        result = num1 + num2
        print (result)

    elif user_choice == "2":
        result = num1 - num2
        print (result)

    elif user_choice == "3":
        result = num1*num2
        print (result)

    else:
        print ("Incorrect option")
    
    menu_list = "Select option:\n1.add\n2.minus\n3.multiple\n0.exit"
    user_choice = input(menu_list)

    




