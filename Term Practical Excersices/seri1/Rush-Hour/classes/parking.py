from classes.car import Car
from copy import deepcopy,copy
from icecream import ic


class Parking:
    def __init__(self, w, h, g = 0, parent= None, cars = []) -> None:
        self.parent = parent
        self.cars: list = cars
        self.main_car: Car = self.get_main_car()
        self.width = w
        self.height = h
        self.parking = self.make_parking()
        self.generate_parking()
        self.next_states = []
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        
    def heuristic(self):
        end_x = int(self.main_car.end[0])
        end_y = int(self.main_car.end[1])
        h = 0
        if self.main_car.orientation == "v":
            for i in range(end_x + 1, self.height):
                if self.parking[i][end_y] != "-":
                    h += 1
                
                    
        if self.main_car.orientation == "h":
            for i in range(end_y + 1, self.height):
                if self.parking[end_x][i] != "-":
                    h += 1
        return h
    
    def check_goal(self):
        if self.main_car.orientation == "v" and self.main_car.end[0] == self.height - 1:
            return True
        elif self.main_car.orientation == "h" and self.main_car.end[1] == self.width - 1:
            return True
        return False
            
    def get_main_car(self):
        for car in self.cars:
            if car.is_main:
                return car
        
        
    def make_parking(self):
        return [[ "-" for _ in range(self.width)] for _ in range(self.height)]
    
    def remove_car(self, car: Car):
        self.cars.remove(car)
        self.generate_parking()
            
    def add_car(self, car):
        self.cars.append(car)
        self.generate_parking()
        
   
    def check_if_valid(self, x, y):
        if 0 <= y < self.width and 0 <= x < self.height and self.parking[int(x)][int(y)] == "-":
            return True
        return False
        
    
    def generate_next_states(self):
        for car in self.cars:
            temp_cars: list = copy(self.cars)
            temp_car: Car = deepcopy(car)
            
            temp_car.move_backward()
            if self.check_if_valid(x=temp_car.start[0], y=temp_car.start[1]):
                temp_cars.remove(car)
                temp_cars.append(temp_car)
                self.next_states.append(Parking(w=self.width, h=self.height, g=self.g + 1, parent=self,  cars=temp_cars))
                
            temp_cars: list = copy(self.cars)
            temp_car: Car = deepcopy(car)
            
            temp_car.move_forward()
            if self.check_if_valid(x=temp_car.end[0], y=temp_car.end[1]):
                temp_cars.remove(car)
                temp_cars.append(temp_car)
                self.next_states.append(Parking(w=self.width, h=self.height, g=self.g + 1, parent=self, cars=temp_cars))
       
    def generate_parking(self):      
        for car in self.cars:
            car: Car = car
            car.cells_occupied()
            for cell in car.occupied:
                cell = cell.split(",")
                self.parking[int(cell[0])][int(cell[1])] = str(car.carnum)
    
    def get_string_version(self):
        string = ""
        for row in self.parking:
            for char in row:
                string += char
        return string
    
    def show_parking(self): 
        self.generate_parking()
        ic(self.parking)