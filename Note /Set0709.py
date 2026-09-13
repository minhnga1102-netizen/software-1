#an unordered data structure (items can occur in any order)
#cannot be referenced with an index
#same item can occur only 1 in set: {}

my_list = [1,2,3,3,4,4]
print(my_list)
print(my_list[0])

#automatically remove same items
#error when trying to search item through index in set
my_set = {1,2,3,3,4,4}
print(my_set)
#print(my_set[0])

#when to use SET instead of LIST?
#only want search/automatic remove an item, no concern in order:
my_list = [1,2,3,3,4,4]
#turn a list into set to automatic remove repetitive items
unique_numbers_list = set(my_list)
print(unique_numbers_list)

#material example:
#different order compared to input set 
games = {'monopoly','chess','cluedo'}
print(games)

#add an item, still unordered set result
games.add('dominion')
print(games)

#remove an item, still unordered set result
games.remove('chess')
print(games)

#add an item, but that item already in list - automatic pass through
games.add("cluedo")
print(games)

for g in games:
    print(g)

#an empty set:
names = set()
names.add("mary")
print(names)