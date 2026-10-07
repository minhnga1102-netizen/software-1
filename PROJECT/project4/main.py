import json
import os
from models.player import Player
from models.room import Room
from models.item import Item

#when program starts, a player object, few items, room are created:

poke_ball = Item ("Poke Ball", "Basic ball, low catch rate")
great_ball = Item("Great Ball", "Better ball, higher catch rate")
ultra_ball = Item("Ultra Ball", "High Performance Ball, very high catch rate" )

pallet_town = Room("Pallet Town", poke_ball)
pokemon_league = Room ("Pokemon League", ultra_ball)
viridian_forest = Room ("Viridian Forest", great_ball)

rooms= [pallet_town, pokemon_league, viridian_forest]
all_items = [poke_ball,great_ball,ultra_ball]

def find_room (rooms, room_name):
    for room in rooms:
        if room.name.lower() == room_name.lower():
            return room
    return None
def find_item (items, item_name):
    for item in items:
        if item.name.lower() == item_name.lower():
            return item
    return None

#Open intro.txt & instructions.txt in read mode, then print, when opening game
#try-except: in case there is no file/typeError:
#intro & instructions.txt separately: if 1 is missing, another still read
try:
    with open("intro.txt","r") as file:
        intro_text = file.read()
        print(intro_text)
except FileNotFoundError:
    print("Intro file not found.")
except IOError:
    print("Error occurred while handling the file.")

try:
    with open("instructions.txt","r") as file:
        instructions_text = file.read()
        print(instructions_text)
except FileNotFoundError:
    print("Instructions file not found.")
except IOError:
    print("Error occurred while handling the file.")


name = input("Please enter your name: ")
age = int(input ("Please enter your age: "))

if age < 12:
    print("You are a minor")
    #create a player Object
else:
    player = Player(name, pallet_town)
    print(f"Hello, {name}")

    file_name = f"save_{name.lower()}.json"
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            save_data=json.load(file)

        player.pokemon_list=save_data["pokemon_list"]
        found_room = find_room(rooms, save_data['location'])
        if found_room is not None:
            player.location = found_room
        
        for item_name in save_data['items']:
            item = find_item(all_items, item_name)
            if item is not None:
                player.items.append(item)

        # items player already has, must disappear from rooms
        for item in player.items:
            for room in rooms:
                if room.item == item:
                    room.item = None
    while True:
        print("====MENU====")
        print("1. POKEDEX - View the Pokemon you have caught")
        print("2. CATCH - Try to catch a wild Pokemon")
        print("3. ITEM - Collect an item from this room")
        print("4. INVENTORY - View your inventory")
        print("5. MOVE - Move to another room")
        print("6. SAVE - Save your game")
        print("7. LOPETA - quit the game")
    
        command = input("Enter a command: ").upper()

        if command == "POKEDEX":
            player.show_pokemon_list()
            
        elif command == "CATCH":
            player.catch_pokemon()
            
        elif command == "ITEM":
            player.collect_item()

        elif command == "INVENTORY":
            player.show_inventory()

        elif command == "MOVE":
            for room in rooms:
                print("-", room.name)

            destination = input("Move to: ").lower()
            room = find_room(rooms, destination)
            if room is not None:
                player.move(room)
            else:
                print("Room not found.")

        elif command == "SAVE":
            #as items is list of object Item - JSON cannot save
            #need to save item.name - create an empty list 
            item_names = []
            for item in player.items:
                item_names.append(item.name)
            #if data (str,list:JSON ok). #need to turn into str, list
            save_data = {
                "name": player.name,
                "location": player.location.name,
                "items": item_names,
                "pokemon_list": player.pokemon_list
            }
           
            file_name = f"save_{player.name.lower()}.json"
            with open(file_name, "w") as file:
                json.dump(save_data, file)
            print("Game saved.")

        elif command == "LOPETA":
            print(f"Thank you, {name}. Good bye!")
            break
        else:
            print("Unknown command. Please try again.")