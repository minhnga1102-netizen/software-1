names = []

names.append ("Nga")
names.append ("Adam")
print(names)

names.remove("Adam")
print(names)\


names.insert(-1,"Micah")
print(names)


names.extend(['micah','jensen'])
print(names)

another_list_of_names = ['katie','nam']
names.extend(another_list_of_names)
print(names)

#index of 1st occurence in array if have duplicates in list
print(names.index("micah"))

if "micah" in names:
    print("Micah found in names list")
else:
    print("Micah not found")

#for LOOP, no need to check conditions as WHILE loop
#index
i = 0
for name in names:
    print(i)
    print(name)
    print(f"value at index {i} is {name}")
    i += 1

#interate 5 times 0-4
print(range(1000))

#not include 10
for i in range (2,10):
    print (i)

#1st: start, 2nd end, 2 is increment
#or *(5,0,-1)/ (10,21,2)
for i in range (0, 10, 3):
    print (i)

names = []
print ("Give 5 names: ")

for i in range (5):
    name = input ("Name: ")
    names.append (name)

print(names)


for i in range (6):
    print ("hello")