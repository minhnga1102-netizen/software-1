#user age <12 - minor, shut down
#else: greet user, display menu until user "lopeta"
#add commands, each: # output
#after each command, display menu again

import random

name = input ("Please enter your name: ")
age = int(input ("Please enter your age: "))


if age < 12:
    print("You are a minor")
else:
    print(f"Hello, {name}")
#While True create a loop run forever as True never becomes False on its own
# need BREAK - loop keep showing menu & ask for command infinitely
# until BREAK
    while True:
        print("====MENU====")
        print("1. POKEDEX - View your pokedex")
        print("2. CATCH - Try to catch a wild Pokemon")
        print("3. LOPETA - quit the game")

        command = input("Enter a command: ").upper()

        if command == "POKEDEX":
            print("Pokedex: Pikachu, Charmander, Bulbasaur, Squirtle.")

        elif command == "CATCH":
            pokemons = ["Pikachu", "Eeve", "Snorlax"]
            caught = random.choice(pokemons)
            print(f"A wild {caught} pokemon has appeared and you caught it!")

        elif command == "LOPETA":
            print(f"Thank you, {name}. Good bye!")
            break

        else:
            print("Unknown command. Please try again.")