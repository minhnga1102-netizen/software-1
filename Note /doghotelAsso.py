class Dog:
    def __init__(self,name):
        self.name=name
    def bark(self):
        print("Bark")

dog=Dog("MusMti")
dog2=Dog("John")

#print BARK when calling the function bark()
dog.bark()
#print NONE as the function bark() has no return value
print(dog.bark())


class GroomingService:
    


class Hotel:
    def __init__(self):
        self.dogs=[]

    def add(self, dog):
        self.dogs.append(dog)
    def print_customers(self):
        for dog in self.dogs:
            print("   "+ dog.name)

hotel_cali = Hotel()
hotel_cali.print_customers()
hotel_cali.add(dog)
hotel_cali.print_customers()
hotel_cali.add(dog2)
hotel_cali.print_customers()

 