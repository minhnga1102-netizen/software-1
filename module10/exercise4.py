import random
class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate=license_plate
        self.maximum_speed=maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate (self, change_of_speed):
        self.current_speed = change_of_speed + self.current_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed=self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + hours*self.current_speed


class Race:
    #self is the object/instance itself created by this class
    #name, distance: temporary property, chi ton tai trong init
    def __init__(self, name, distance, cars):
        #luu vao object cac bien/properties de dung lau dai
        #gan lien voi object nay, nen khi goi: self.name(car1.name)
        self.name = name
        self.distance=distance
        self.cars=cars
    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
    def print_status(self):
        #print name, distance of the race itself
        #VD RED BULL 9000km
        print(f"{self.name} {self.distance} km")
        #print the title row of the table (Plate, CurrentSpeed, TravelledDistance)
        print(f"{"Plate":<10} {"Speed":>10}{"Distance:>15"}")
        #print details of each car participating the race
        for car in self.cars:
            print(f"{car.license_plate:<10} {car.current_speed:>10}{car.travelled_distance:>15}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


        