number = int(input("Enter an integer: "))

#prime number: /1 or /number = 0
#as a number always /1 = 0 & /itself = 0
#if number / any other number = 0 -> not prime (2,3...,number-1)
#if not: prime

#test number = 0, 1 - print as a prime number - WRONG
#add more condition to check if number < 2 (0,1)

if number < 2:
    print (f"{number} is not a prime number.")
else: 
    is_prime = True
#print RESULT only after the loop for run completely
#need assign True/False
#then True, print as a prime and False, print not a prime
    for i in range (2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:   
        print (f"{number} is not a prime number.")