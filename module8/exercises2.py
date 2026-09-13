#ask user to enter names until they enter empty STR
#print New name or Existing name
#finally, print names one by one, in any order
#use set data structure to store names

name = input("Please enter a name (Enter to quit): ")
#create an empty set
names = set()

while name != "":     
    if name in names:
        break
    #check if name is in names, before adding!
        print("Existing name.")
    else:
        print("New name.")
        names.add(name)
print(names)