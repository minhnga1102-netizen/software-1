import random

class Car:
    def __init__ (self,license_plate,maximum_speed):
        self.license_plate=license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance=0
        
    def accelerate(self,change_of_speed):
        self.current_speed=change_of_speed +self.current_speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed=self.maximum_speed
            
        
    def drive(self,hours):
        self.travelled_distance=self.travelled_distance + hours*self.current_speed
        
def race(cars):
    while True:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)
        if car.travelled_distance >= 10000:
            break
    return cars