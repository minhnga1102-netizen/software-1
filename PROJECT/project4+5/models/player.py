import random

class Player:
    def __init__(self, name, location):
        self.name=name
        self.items = []
        # a new player starts with no pokemon
        self.pokemon_list = []
        self.location = location
    def move(self, room):
        self.location = room
        print(f"You have moved to {room.name}")
    def collect_item(self):
        #if current room has an item, add it to player's items
        if self.location.item is not None:
            self.items.append(self.location.item)
            print(f"{self.location.item.name} has been added to your list.")
            #the room is now empty
            self.location.item = None
        else:
            print("There is nothing in the room.")
    def show_inventory(self):
        if len(self.items) == 0:
           print("Your items list is empty.")
        else: 
           for item in self.items:
                print(f"{item.name} {item.effect}")

    #show user's caught pokemon
    def show_pokemon_list(self):
        if len(self.pokemon_list) == 0:
            print("Your pokemon list is empty.")
        else:
            for pokemon in self.pokemon_list:
                print(pokemon)

    def catch_pokemon(self,all_pokemon):
        # pick a random pokemon, add it only if the player does not have it yet
        caught = random.choice(all_pokemon)
        if caught in self.pokemon_list:
            print(f"A wild {caught} pokemon has appeared, but you already have it.")
        else:
            print(f"A wild {caught} pokemon has appeared and you caught it!")
            self.pokemon_list.append(caught)