class Player:
    def __init__(self, name, level, items, room):
        self.name= name
        self.level=level
        self.items=items
        self.room = room

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price=price

class Room:
    def __init__(self, name, description):
        self.name=name
        self.description=description
        self.items=[]



item1= Item("sword",123)
item2= Item("shield", 456)
items = [item1, item2]
player1=Player("Mia",0,items)
print(player1.items)