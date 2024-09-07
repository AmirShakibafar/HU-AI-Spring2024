import numpy as np

class Car:
    def __init__(self, carnum, orientation, main=False) -> None:
        self.carnum = carnum
        self.start = np.zeros(2)
        self.end = np.zeros(2)
        self.is_main = main
        self.orientation = orientation
        self.occupied = []
        
    def set_start(self, x, y):
        self.start[0] = x  
        self.start[1] = y  
    
    def get_start(self):
        return self.start
    
    def set_end(self, x, y):
        self.end[0] = x
        self.end[1] = y
        self.cells_occupied()

    def get_end(self):
        return self.end
      
    def cells_occupied(self):
        self.occupied.clear()
        car_x = int(self.start[0])
        car_y = int(self.start[1])
        while car_x <= self.end[0] and car_y <= self.end[1]:
            self.occupied.append(f"{car_x},{car_y}")
            if self.orientation == "v":
                car_x += 1
            elif self.orientation == "h":
                car_y += 1
    
    def move_forward(self):
        
        start_x = self.start[0]
        start_y = self.start[1]
        end_x = self.end[0]
        end_y = self.end[1]
        
        if self.orientation == "h":
            start_y += 1
            end_y += 1
        elif self.orientation == "v":
            start_x += 1
            end_x += 1
        
        self.start = np.array([start_x, start_y])
        self.end = np.array([end_x, end_y])
        self.cells_occupied()
    
    def move_backward(self):
        
        start_x = self.start[0]
        start_y = self.start[1]
        end_x = self.end[0]
        end_y = self.end[1]
        
        if self.orientation == "h":
            start_y -= 1
            end_y -= 1
            
        elif self.orientation == "v":
            start_x -= 1
            end_x -= 1
        
        # if end_x >= 0 and end_y >= 0 and start_x >= 0 and start_y >= 0:
        self.start = np.array([start_x, start_y])
        self.end = np.array([end_x, end_y])
        self.cells_occupied()