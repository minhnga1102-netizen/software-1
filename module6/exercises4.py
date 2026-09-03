# no need this line, otherwise ask user 6 times
# city = input("Enter the name of a city: ")

cities = []

for i in range (5):
    city = input("Enter the name of a city: ")
    cities.append(city)

#this line print an array: print(cities)

print("The cities you entered:")

for city in cities:
    print (city)