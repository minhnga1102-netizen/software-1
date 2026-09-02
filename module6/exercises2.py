number = input("Enter a number: ")

numbers = []

while number == '':
    numbers.append(int(number))
    number = input("Enter a number: ")

print (numbers)