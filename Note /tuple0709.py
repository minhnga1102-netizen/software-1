#Tuple: list of ordered items but cannot be modified 
#() instead of []
#index starting from 0, same as list

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday")
days_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[days_number-1]
print(f"Day number {days_number} is {day}.")

#Tuple unpacking
fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits
print(f"The fruits are: {first}, {second}, and {third}")

#Tuple as return values
import random
def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first,second

die1, die2 = cast()
print(f"The dice show {die1} and {die2}.")