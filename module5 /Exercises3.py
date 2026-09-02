
# # pseudo code 
# 1. ask user input (str)
#     assign count = 0 (not run yet any round)
#     assing smallest, largest = NONE (not empty str, later number)
# 2. Check while input # '' (empty string) - execute code
#     turn str into number using float

#     ASSign 1st number = smallest, largest
#         if count == 0 (compare ==, not assign =)
#         smallest/largest = number   

#     ELSE:
#         if number < smallest ->
#         if number > largest ->

# 3. Print
    
smallest = None
largest = None
count = 0
user_input = input ('Enter a number (or press Enter to quit): ')

while user_input != '':
    number = float (user_input)

    if count == 0:
        smallest = number
        largest = number

    else: 
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    count +=1
    user_input = input ('Enter a number (or press Enter to quit): ')


print (f"Smallest number: {smallest}\nLargest number: {largest}")