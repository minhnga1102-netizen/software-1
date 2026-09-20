import random

inventory = []

def show_pokedex():
    print("Pokedex: Pikachu, Charmander, Bulbasaur, Squirtle.")

def catch_pokemon():
    pokemons = ["Pikachu", "Eeve", "Snorlax"]
    caught = random.choice(pokemons)
    print(f"A wild {caught} pokemon has appeared and you caught it!")
    
def add_item():
    item = input("Enter the name of the item you found: ")
    inventory.append(item)
    print(f"{item} has been added to your list.")

def show_inventory():
    if len(inventory) == 0:
        print("Your inventory is empty.")
    else: 
        for item in inventory:
            print(item)

name = input ("Please enter your name: ")
age = int(input ("Please enter your age: "))

if age < 12:
    print("You are a minor")
else:
    print(f"Hello, {name}")

    while True:
        print("====MENU====")
        print("1. POKEDEX - View your pokedex")
        print("2. CATCH - Try to catch a wild Pokemon")
        print("3. ITEM - Add an item to your inventory")
        print("4. INVENTORY - View your inventory")
        print("5. LOPETA - quit the game")

        command = input("Enter a command: ").upper()

        if command == "POKEDEX":
            show_pokedex()

        elif command == "CATCH":
            catch_pokemon()

        elif command == "ITEM":
            add_item()

        elif command == "INVENTORY":
            show_inventory()

        elif command == "LOPETA":
            print(f"Thank you, {name}. Good bye!")
            break
        else:
            print("Unknown command. Please try again.")