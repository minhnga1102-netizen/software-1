#1. STRUCTURE: main program + function
#define-def + name of function + (parameters): 

def greet():
    print("hello")
    return

#2. CALL a function
greet()

#3. PARAMETERS
def greet (times):
    for i in range (times):
        print("hello")
    return
greet(5)

#4.VARIABLE scope
#local/global variable inside/outside function
city = "Helsinki"
print("at the beginning of program: " + city)

def change():
    city = "Vantaa"
    print("at the end of function, " +city)
    return

change()

print("at the end of program: " + city)

#5 MULTIPLE PARAMETERS
def greet (greeting, times):
    for i in range (times):
        print(greeting + " round: " + str(i+1))
    return

greet("hello",3)

#6. RETURN VALUE
def sum_of_squares(first, second):
    result = first**2 + second**2
    return result
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = sum_of_squares
