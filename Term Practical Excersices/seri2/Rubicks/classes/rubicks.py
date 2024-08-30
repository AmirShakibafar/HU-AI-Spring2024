from icecream import ic
from copy import deepcopy


cube = {
    "blue": [f"{i}_blue" for i in range(8)],
    "green": [f"{i}_green" for i in range(8)],
    "white": [f"{i}_white" for i in range(8)],
    "orange": [f"{i}_orange" for i in range(8)],
    "red": [f"{i}_red" for i in range(8)],
    "yellow": [f"{i}_yellow" for i in range(8)],
}

class RubicksCube:
    def __init__(self, cube, g=0, move_that_created=None, parent=None) -> None:
        self.cube: dict = cube
        self.top = "yellow"
        self.bottom = "white"
        self.front = "green"
        self.left = "red"
        self.right = "orange"
        self.back = "blue"

        self.parent = parent
        self.move_that_created = move_that_created
        self.next_states = []
        self.g = g
        # we add h later
        self.f = g

    def heuristic(self):
        
        
        path_cost = {
            "blue": {"orange": 1, "red": 1, "green": 2, "white": 1, "blue": 0, "yellow": 1},
            "red": {"blue": 1, "orange": 2, "white": 1, "green": 1, "red": 0, "yellow": 1},
            "orange": {"blue": 1, "red": 2, "yellow": 1, "white": 1, "orange": 0, "green": 1},
            "green": {"blue": 2, "orange": 1, "white": 1, "red": 1, "green": 0, "yellow": 1},
            "white": {"red": 1, "blue": 1, "green": 1, "orange": 1, "white": 0, "yellow": 2},
            "yellow": {"white": 2, "orange": 1, "blue": 1, "green": 1, "yellow": 0, "red": 1}
        }
        cost = 0
        for face in self.cube.keys():
            for block in self.cube[face]:
                cost += path_cost[face][block]
        cost /= 12
        cost = int(cost)
        self.f += cost
    
    def check_goal(self):
        # Iterate through each face of the cube
        for blocks in self.cube.values():
            # checks if all blocks on the side have the same color
            if len(set(blocks)) != 1:
                return False
        return True

    def generate_next_states(self):
        # Create a deepcopy of the current cube configuration
        curr_cube = deepcopy(self.cube)
    
        # Generate next states for each possible rotation
        self.L_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="L", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.L_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="L'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.R_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="R", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.R_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="R'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.U_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="U", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.U_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="U'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.D_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="D", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.D_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="D'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.F_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="F", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.F_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="F'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.B_rotate()
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="B", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)

        self.B_rotate(reverse=True)
        Rubick = RubicksCube(cube=self.cube, g=self.g+1, move_that_created="B'", parent=self)
        self.next_states.append(Rubick)
        self.cube = deepcopy(curr_cube)


    
    def generate_string_version(self):
        string_version = ""
        # sides = ["🟨", "🟩", "⬜️", "🟦", "🟥", "🟧"]
        sides = ["blue", "green", "white", "red", "yellow", "orange"]

        for side in sides:
            string_version += f"{side}:"
            blocks = self.cube[side]
            grid = [blocks[i:i+3] for i in range(0, len(blocks), 3)]
            for row in grid:
                string_version += "".join(row)

        return string_version

    
    def print_cube(self):
        
        for side in self.cube.keys():
            list_side = self.cube[side]
            ic(side)
            ic(list_side[0:3])
            ic(list_side[3:6])
            ic(list_side[6:9])
            ic(" ")
            
            
    def swapper(self, side1, side2, index1, index2):
        side1[index1], side2[index2] = side2[index2], side1[index1] 
          
    def swapper_sides(self, side1_key, side2_key, idx1, idx2, idx3, idx4, idx5, idx6):
        side1 = self.cube[side1_key]
        side2 = self.cube[side2_key]
        self.swapper(side1, side2, idx1, idx4)
        self.swapper(side1, side2, idx2, idx5)
        self.swapper(side1, side2, idx3, idx6)
    
    def helper_inside_rotation(self, side, index1, index2, index3, index4):
        side[index1], side[index2] = side[index2], side[index1]
        side[index1], side[index3] = side[index3], side[index1]
        side[index1], side[index4] = side[index4], side[index1]
           
    def inside_rotation(self, side_key, reverse=False):
        side = self.cube[side_key]
        
        # this is for swapping the inside
        if reverse:
            self.helper_inside_rotation(side, 6, 8, 2, 0)
            self.helper_inside_rotation(side, 3, 7, 5, 1)
        else:
            self.helper_inside_rotation(side, 0, 2, 8, 6)
            self.helper_inside_rotation(side, 1, 5, 7, 3)
            
    def L_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.left)
            self.swapper_sides(self.front, self.bottom, 0, 3, 6, 0, 3, 6)
            self.swapper_sides(self.front, self.back, 0, 3, 6, 8, 5, 2)
            self.swapper_sides(self.front, self.top, 0, 3, 6, 0, 3, 6)
        else:
            self.inside_rotation(self.left, True)
            self.swapper_sides(self.front, self.top, 0, 3, 6, 0, 3, 6)
            self.swapper_sides(self.front, self.back, 0, 3, 6, 8, 5, 2)
            self.swapper_sides(self.front, self.bottom, 0, 3, 6, 0, 3, 6)
    
    def R_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.right, True)
            self.swapper_sides(self.front, self.top, 2, 5, 8, 2, 5, 8)
            self.swapper_sides(self.top, self.bottom, 2, 5, 8, 2, 5, 8)
            self.swapper_sides(self.top, self.back, 2, 5, 8, 6, 3, 0)
        else:
            self.inside_rotation(self.right)
            self.swapper_sides(self.front, self.bottom, 2, 5, 8, 2, 5, 8)
            self.swapper_sides(self.bottom, self.top, 2, 5, 8, 2, 5, 8)
            self.swapper_sides(self.bottom, self.back, 2, 5, 8, 6, 3, 0)
            
    def U_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.top, True)
            self.swapper_sides(self.front, self.right, 0, 1, 2, 0, 1, 2)
            self.swapper_sides(self.front, self.back, 0, 1, 2, 0, 1, 2)
            self.swapper_sides(self.front, self.left, 0, 1, 2, 0, 1, 2)
        else:
            self.inside_rotation(self.top)
            self.swapper_sides(self.front, self.left, 0, 1, 2, 0, 1, 2)
            self.swapper_sides(self.front, self.back, 0, 1, 2, 0, 1, 2)
            self.swapper_sides(self.front, self.right, 0, 1, 2, 0, 1, 2)
    
    def D_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.bottom)
            self.swapper_sides(self.front, self.right, 6, 7, 8, 6, 7, 8)
            self.swapper_sides(self.front, self.back, 6, 7, 8, 6, 7, 8)
            self.swapper_sides(self.front, self.left, 6, 7, 8, 6, 7, 8)
        else:
            self.inside_rotation(self.bottom, True)
            self.swapper_sides(self.front, self.left, 6, 7, 8, 6, 7, 8)
            self.swapper_sides(self.front, self.back, 6, 7, 8, 6, 7, 8)
            self.swapper_sides(self.front, self.right, 6, 7, 8, 6, 7, 8)        
    
    def F_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.front)
            self.swapper_sides(self.right, self.top, 0, 3, 6, 6, 7, 8)
            self.swapper_sides(self.top, self.bottom, 6, 7, 8, 2, 1, 0)
            self.swapper_sides(self.top, self.left, 6, 7, 8, 8, 5, 2)
        else:
            self.inside_rotation(self.front, True)
            self.swapper_sides(self.left, self.top, 2, 5, 8, 8, 7, 6)
            self.swapper_sides(self.top, self.bottom, 6, 7, 8, 2, 1, 0)
            self.swapper_sides(self.top, self.right, 6, 7, 8, 0, 3, 6)
            
    def B_rotate(self, reverse=False):
        if not reverse:
            self.inside_rotation(self.back)
            self.swapper_sides(self.top, self.left, 0, 1, 2, 6, 3, 0)
            self.swapper_sides(self.top, self.bottom, 0, 1, 2, 8, 7, 6)
            self.swapper_sides(self.top, self.right, 0, 1, 2, 2, 5, 8)
        else:
            self.inside_rotation(self.back, True)
            self.swapper_sides(self.left, self.top, 0, 3, 6, 2, 1, 0)
            self.swapper_sides(self.left, self.right, 0, 3, 6, 8, 5, 2)
            self.swapper_sides(self.left, self.bottom, 0, 3, 6, 6, 7, 8)
            
            