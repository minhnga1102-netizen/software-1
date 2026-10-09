#1.PREPARATION: Import & game data (items, rooms, pokemon)
import json
import os
from models.player import Player
from models.room import Room
from models.item import Item

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

poke_ball = Item ("Poke Ball", "Basic ball, low catch rate")
great_ball = Item("Great Ball", "Better ball, higher catch rate")
ultra_ball = Item("Ultra Ball", "High Performance Ball, very high catch rate" )

pallet_town = Room("Pallet Town", poke_ball)
pokemon_league = Room ("Pokemon League", ultra_ball)
viridian_forest = Room ("Viridian Forest", great_ball)

rooms= [pallet_town, pokemon_league, viridian_forest]
all_items = [poke_ball,great_ball,ultra_ball]
all_pokemon = ["Pikachu", "Eevee", "Snorlax","Mewtwo"]


#2. HELPER FUNCTIONS, find an object by its name
def find_room (room_list, room_name):
    for room in room_list:
        if room.name.lower() == room_name.lower():
            #return OBJECT ROOM with this name
            return room
    return None

def find_item (item_list, item_name):
    for item in item_list:
        if item.name.lower() == item_name.lower():
            #return OBJECT ITEM with this name
            return item
    return None


#3. Show intro and instructions 
# (try/except if a file is missing)
try:
    with open(os.path.join(BASE_DIR,"intro.txt"),"r") as file:
        intro_text = file.read()
        print(intro_text)
except FileNotFoundError:
    print("Intro file not found.")

try:
    with open(os.path.join(BASE_DIR,"instructions.txt"),"r")as file:
        instructions_text = file.read()
        print(instructions_text)
except FileNotFoundError:
    print("Instructions file not found.")


#4. ASK NAME & HANDLE AGE
name = input("Please enter your name: ")
while True:
    try: 
        age = int(input ("Please enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be greater than 0.")
    except ValueError:
        print("Please enter a number.")

if age < 12:
    print("You are a minor")
else:
    # create a player Object, current location: pallet town
    player = Player(name, pallet_town)
    print(f"Hello, {name}")

    #5. LOAD SAVED FILE IF IT EXISTS
    # JSON has only text, turn names back into OBJECTS
    file_name = os.path.join(BASE_DIR,f"save_{name.lower()}.json")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            #read file, save_data is a dictionary 
            save_data =json.load(file)
        #restore pokemon which player already caught
        player.pokemon_list=save_data["pokemon_list"]

        #save_data(location) is text, function find_room return OBJECT
        found_room = find_room(rooms, save_data['location'])
        #if room is found, use it as player's location
        if found_room is not None:
            player.location = found_room
            
        for item_name in save_data['items']:
            found_item = find_item(all_items, item_name)
            #add back each saved item as an Item object
            if found_item is not None:
                player.items.append(found_item)

        #remove items player already has from the room
        for item in player.items:
            for room in rooms:
                if room.item == item:
                    room.item = None

    #6. MAIN MENU LOOP: repeats until player types LOPETA or WIN
    while True:
        print("====MENU====")
        print("POKEDEX - View the Pokemon you have caught")
        print("CATCH - Try to catch a wild Pokemon")
        print("ITEM - Collect an item from this room")
        print("INVENTORY - View your inventory")
        print("MOVE - Move to another room")
        print("SAVE - Save your game")
        print("LOPETA - quit the game")
        
        command = input("Enter a command: ").upper()

        if command == "POKEDEX":
            #call PLAYER class method/function
            #to show the pokemon player has caught
            player.show_pokemon_list()
                
        elif command == "CATCH":
            player.catch_pokemon(all_pokemon)
                
        elif command == "ITEM":
            player.collect_item()

        elif command == "INVENTORY":
            player.show_inventory()

        elif command == "MOVE":
            #print list of rooms
            for room in rooms:
                print("-", room.name)
            #ask player where to move next
            destination = input("Move to: ").lower()
            #search for that room by calling the function find_room
            room = find_room(rooms, destination)
            if room is not None:
                player.move(room)
            else:
                print("Room not found.")

        #7 SAVE: write the game data to JSON file
        elif command == "SAVE":
            #JSON can't store ITEM objects so save only item names
            item_names = []
            #loop through items and keep only their names
            for item in player.items:
                #get object name, add to empty list 
                item_names.append(item.name)
            #put together data into a dict
            save_data = {
                "name": player.name,
                #save room.name, not room object
                "location": player.location.name,
                "items": item_names,
                "pokemon_list": player.pokemon_list
                }
            file_name = os.path.join(BASE_DIR,f"save_{player.name.lower()}.json")
            #'w' = write mode, replaces the old save file
            with open(file_name, "w") as file:
                #put dict into JSON file
                json.dump(save_data, file)
            print("Game saved.")

        #8. QUIT & CHECK WINNER:
        elif command == "LOPETA":
            print(f"Thank you, {name}. Good bye!")
            break
        #if the command is wrong
        else:
            print("Unknown command. Please try again.")

        # After every command, check if player won (break ends the game)
        if "Mewtwo" in player.pokemon_list and len(player.items) == len(all_items):
            print("ROUTE 1: Legend Hunter. Congratulations. You caught Mewtwo and collected 3 balls. You win!")
            break
        elif len(player.pokemon_list) == len(all_pokemon):
            print("ROUTE 2: MASTER POKEDEX. Congratulations, you caught all pokemon. You win!")
            break
        elif player.location == pokemon_league and len(player.items) >=2 and len(player.pokemon_list)>=2: 
            print("ROUTE 3: EXPLORER. Congratulations, you reached the Pokemon League with 2 balls and 2 pokemons. You win!")
            break 
        

