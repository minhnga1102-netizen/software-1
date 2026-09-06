# a function parameter = list of integers
# return sum of list
#main program: create list, call function, print out value 


list = [1,2,3,4,5]

def sum_of_list (list):
    total = 0
    for i in list:
        total+=i
    return total

#result = total 
result = sum_of_list(list)

print(f"The sum of the numbers in the list is: {result}")







