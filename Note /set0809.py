#UNORDERED data structure
games = {"chess","puzzle","monopoly","diablo","puzzle"}
print(games)

games.add("cluedo")
print(games)

for i in range(600):
    games.add('cluedo')

for game in games:
    print(game)
print(games)

if "cluedo" in games:
    print ("cluedo found")
games.add("carcassone")

empty_set = {}
print(empty_set)

#call function set to create EMPTY SET
empty_set=set()