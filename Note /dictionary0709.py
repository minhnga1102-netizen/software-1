#one of most common used Python data structure
#store key:value pairs

numbers = {"Vivi":"0438403",
           "Adam": "02348239",
           "mia": "3424"}

#new value can be added by dictionary[key] = value
numbers['micah'] = 'y3we4'
numbers['jensen'] = '3247'

print(numbers)

#also, value can be retrieved by dictionary[key]
name = input("enter name: ")
if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}")