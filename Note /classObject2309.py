class Player:
    def __init__(self, name, level, id):
        self.name=name
        self.level=level
        self.id=id
        #when new object is created, its given an item
        #start with empty list
        self.items = []
    def level_up(self):
        self.level+=1
    def add_item(self, item_name):
        self.items.append(item_name)



player1=Player("Mia",0,123)
player2=Player("Adam",1,456)
player2.level_up()
print(player2.level)
player2.add_item("sword")
print(player2.items)

class Item:
    number_of_items = 0
    def __init__(self, name, description, price):
        self.name=name
        self.description=description
        self.price=price
        Item.number_of_items+=1

item1=Item('table',"eating",123)
print(item1.price)
print(Item.number_of_items)
