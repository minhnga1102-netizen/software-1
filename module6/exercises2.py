number = input("Enter a number: ")

numbers = []

while number != '':
    numbers.append(int(number))
    number = input("Enter a number: ")

#sort list in descending order
numbers.sort(reverse=True)

#print the first 5 numbers of that list
# this line print numbers in array
# print(f"The greatest numbers in descending order: {numbers[0:5]}")

print("The greatest numbers in descending order:")
for number in numbers[0:5]:
    print(f"{number:.1f}")



   
