import random
from models.player import Player
from models.room import Room
from models.item import Item


def show_pokedex():
    print("Pokedex: Pikachu, Charmander, Bulbasaur, Squirtle.")

def catch_pokemon():
    pokemons = ["Pikachu", "Eeve", "Snorlax"]
    caught = random.choice(pokemons)
    print(f"A wild {caught} pokemon has appeared and you caught it!")
    
#when program starts, a player object, few items, room are created:

poke_ball = Item ("Poke Ball", "Basic ball, low catch rate")
great_ball = Item("Great Ball", "Better ball, higher catch rate")
ultra_ball = Item("Ultra Ball", "High Performance Ball, very high catch rate" )

pallet_town = Room("Pallet Town", poke_ball)
pokemon_league = Room ("Pokemon League", ultra_ball)
viridian_forest = Room ("Viridian Forest", great_ball)

rooms= [pallet_town, pokemon_league, viridian_forest]


name = input ("Please enter your name: ")
age = int(input ("Please enter your age: "))

if age < 12:
    print("You are a minor")
    #create a player Object
else:
    player = Player(name, pallet_town)
    print(f"Hello, {name}")

    while True:
        print("====MENU====")
        print("1. POKEDEX - View your pokedex")
        print("2. CATCH - Try to catch a wild Pokemon")
        print("3. ITEM - Collect an item from this room")
        print("4. INVENTORY - View your inventory")
        print("5. MOVE - Move to another room")
        print("6. LOPETA - quit the game")

        command = input("Enter a command: ").upper()

        if command == "POKEDEX":
            show_pokedex()

        elif command == "CATCH":
            catch_pokemon()

        elif command == "ITEM":
            player.collect_item()

        elif command == "INVENTORY":
            player.show_inventory()

        elif command == "MOVE":
            #rooms is a list of OBJECTS, not str, cant compare input str vs object
            #need to get room.name (str) out of that list to compare
            room_names = []
            for room in rooms:
                room_names.append(room.name.lower())
                print("-", room.name)

            destination = input("Move to: ").lower()

            #now comparing str vs str, both lowercase
            if destination in room_names:
                for room in rooms:
                    if room.name.lower() == destination:
                        player.move(room)
            else:
                print("Room not found.")
        elif command == "LOPETA":
            print(f"Thank you, {name}. Good bye!")
            break
        else:
            print("Unknown command. Please try again.")