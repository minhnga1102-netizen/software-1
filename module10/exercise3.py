class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self):
        self.current_floor += 1
    def floor_down(self):
        self.current_floor -= 1
    def go_to_floor(self,floor):
        while self.current_floor < floor:
            self.floor_up()
        while self.current_floor > floor:
            self.floor_down()
class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range (number_of_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)
    def run_elevator (self, elevator_index, floor):
        chosen_elevator = self.elevators[elevator_index]
        chosen_elevator.go_to_floor(floor)
    def fire_alarm (self):
        for elevator in self.elevators: 
            elevator.go_to_floor(self.bottom_floor)
        