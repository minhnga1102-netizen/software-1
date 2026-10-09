# POKEMON GAME
Minh Nga Nguyen

- 0109: I did project2 assignment
- 2009: I did project3 assignment
- 2709: I did project4 assignment
- 0910: I did project5 assignment

# GAME IDEA

This game is about a Pokemon world.
The player is a trainer starting his journey: explore new places, collect poke balls, and catch wild pokemon.
Player plays by typing the command in the menu.
The game supports SDG 15 - Life on Land.

# Sustainable Development Goal

The game takes **SDG 15 - Life on Land** into account. The player is a trainer who explores nature, for example Viridian Forest, and learns that wild Pokemon and their homes must be protected. There is no fighting or hurting in the game: Pokemon are caught gently and added to the Pokedex. The intro text reminds the player to respect wildlife and forests.


# Objective

Win the game in 3 ways:

- Route 1 - Legend Hunter: Catch the legendary Pokemon Mewtwo and collect all 3 balls.
- Route 2 - Master Pokedex: catch all 4 pokemon.
- Route 3 - Explorer: reach the Pokemon League with at least 2 pokemon and 2 balls.

# How the game works

1. The game shows the intro and instructions.
2. Player enters their name and age. If there is a saved file with the same name, that file is loaded.
3. Player types command in main menu. After each command, game checks if the player has won:
   - Route 1: Legend Hunter: Catch Mewtwo and collect all 3 balls. Each ball is in different room so player needs to visit all rooms.
   - Route 2: Master Pokedex: Catch all Pokemon.
   - Route 3: Explorer: Go to Pokemon League with at least 2 balls and 2 pokemon. 

# Functionalities

Command & what it does:

- Pokedex: Show the pokemon list you have caught
- Catch: player tries to catch a wild Pokemon
- Item: Collects the item inside the current room
- Inventory: Show your list of items
- Move: Moves to another room
- Save: Save your game
- Lopeta: Quit the game

**Other features**

- Asks for player's name and age (under 12 are told they are a minor and game ends)
- Intro and instructions are read from text files
- Save and load by the player's name, in `save_<name>.json`
- Random Pokemon catching, the same Pokemon cannot be caught twice
- There are total 3 ways to win.

# K12

The game has no violence and suitable for children above 12.

# Project Structure

- `main.py`: Main program
  - It creates rooms, all items, and a pokemon list
  - It has functions find_room(), find_item(), and runs the main menu loop

**Classes**

- `models/item.py`: Item class, represents an item (a ball) in the game
  - attributes: name, effect (description)
- `models/room.py`: Room class, represents a location in the game
  - attributes: name and item (None if empty or 1 item currently in this room)
- `models/player.py`: Player class, represents a player in the game
  - attributes: name, items (inventory list), location (current room), pokemon_list (caught Pokemon)
  - methods: move(), collect_item(), show_inventory(), show_pokemon_list(), catch_pokemon(all_pokemon)

# File handling

- `intro.txt`: the welcome text shown when the game starts
- `instructions.txt`: instructions to commands shown in the game. If 1 file is missing, a message is printed and the game continues
- `save_<name>.json`: saved game when user types SAVE command. When the game starts, user types their name. If a file with that name exists, the game loads it and the player can continue where they left off.