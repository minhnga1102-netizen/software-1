
# POKEMON GAME
Minh Nga Nguyen

0109 I did project2 assignment

2009 I did project3 assignment 

2709 I did project4 assignment

# Project Structure
main.py: Main program 

CLASSES

models/item.py: Item class, represent an item in the game with attributes: name, effect (description)

models/room.py: Room class, represent a location in the game with attributes: name and item (None if empty or 1 item currently in this room)

models/player.py: Player class, represent a player in the game with 
- attributes: name, items (inventory list), location (current room) 
- methods: move(), collect_item(), show_inventory()
