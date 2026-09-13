# # #Tuple: immutable, cannot be changed (add, remove)
# # days_of_the_week = ("Monday", "Tuesday", "Wednesday")
# # print(days_of_the_week)

# # #index starting from 0, same as LIST
# # print(days_of_the_week[0])
# # print(days_of_the_week[-1])

# # print(len(days_of_the_week))
# # print(len(days_of_the_week)-1)

# # #how many times "argument" exits. Count function!
# # print(days_of_the_week.count("Monday"))
# # print(days_of_the_week.index("Monday"))

# days_of_the_week = ()

# print(days_of_the_week)
# print(len(days_of_the_week))

# days_of_the_week = ("Monday", "Tuesday", "Wednesday")

# print(days_of_the_week[0:1])
# print(days_of_the_week[1:])

# fruits = "orange", 'apple', 'banana'
# #unpacking tuple
# first, second, third = fruits
# print(f"The fruits are: {first}, {second}, and {third}.")
# print(first)
# print(fruits)
# print(fruits[0:1])
# print(fruits[1:])

# #Nested tuple
# values1 = 1, 2, 3, 4, 5
# values2 = 1, 2, (3, 4), 5
# values3 = (1,2,3,4)
# values4 = (1, 2, (3, 4), 5)
# print(values1)
# print(values2)
# print(values3)
# print(values4)


import random
def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first, second

value = cast()
print(value)