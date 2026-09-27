class Player:
    def __init__(self, name, location):
        self.name=name
        self.items = []
        #instance attribute, always come with SELF
        self.location = location
    def move(self, room):
        self.location = room
        print(f"You have moved to {room.name}")
    def collect_item(self):
        #if there is some items in ROOM, add to player's list
        #item here is attribute of ROOM class
        if self.location.item is not None:
            #add that item to Player's list (items[])
            self.items.append(self.location.item)
            print(f"{self.location.item.name} has been added to your list.")
            self.location.item = None
        else:
            print("There is nothing in the room.")
    def show_inventory(self):
        if len(self.items) == 0:
           print("Your list is empty.")
        else: 
           for item in self.items:
                print(f"{item.name} {item.effect}")