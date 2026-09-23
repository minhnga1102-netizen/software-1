import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed=change_of_speed +self.current_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance=self.travelled_distance + hours* self.current_speed
        

def race(cars):
    while True:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
        if car.travelled_distance >= 10000:
            break
    return cars
    




# car1 = Car ("ABS-123",142)
# print(f"License plate: {car1.license_plate}\nMaximum speed: {car1.maximum_speed}")
# print(f"Current speed: {car1.current_speed}\nTravelled distance: {car1.travelled_distance}")
# car1.accelerate(200)
# print(f"Current speed: {car1.current_speed} km/h")
# car1.accelerate(-100)
# print(f"Current speed: {car1.current_speed} km/h")
# print(f"Initial distance: {car1.travelled_distance} km")
# car1.current_speed= 60
# car1.drive(2)
# print(f"Distance after driving 2 hours at 60 km/h is {car1.travelled_distance}")