from icecream import ic
from copy import deepcopy

class Constraint:
    def __init__(self, variables: list):
        self.variables = variables
        self.assigned = 0
        
    def satisfied(self, assignment: dict) -> bool:
        for var1 in self.variables:
            for var2 in self.variables:
                if var1 == var2:
                    continue
                #check if both variables are assigned
                if var1 in assignment and var2 in assignment:
                    #if both variables have the same value, constraint is violated
                    if assignment[var1] == assignment[var2]:
                        return False    
        return True
        
    
class Sudoku:
    def __init__(self, board):
        self.board: list[list[int]] = board
        self.variables = [f"{x},{y}"  for x in range(9) for y in range(9)]
        self.domains = {}
        self.constraints: set = {}
        
        for var in self.variables:
            self.constraints[var] = []
            self.domains[var] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            
    def add_constraint(self, constraint: Constraint):
        for var in constraint.variables:
            self.constraints[var].append(constraint) 
                   
    def make_consistant(self, assignment):
        for var in assignment:
            list_of_constraints = self.constraints[var]
            for constraint in list_of_constraints:
                for variable in constraint.variables:
                    if variable == var:
                        continue
                    if assignment[var] in self.domains[variable]:
                        self.domains[variable].remove(assignment[var])
        
    def consistent(self, variable, assignment) -> bool:
        # checking to see if any constraint is violated
        for constraint in self.constraints[variable]: 
            if not constraint.satisfied(assignment):                
                return False
        return True  
    
    def backtracking_search(self, assigment):
        if len(assigment) == len(self.variables):
            return assigment
        #choosing what to assign next
        unassigned = [v for v in self.variables if v not in assigment]
        first_var = unassigned[0]
        
        for value in self.domains[first_var]:
            local_assignment = deepcopy(assigment)
            local_assignment[first_var] = value
            if self.consistent(variable=first_var, assignment=local_assignment):
                result = self.backtracking_search(assigment=local_assignment)
                if result is not None:
                    return result
                
        return None
    
    def print_final_board(self, assignment):
        if not assignment:
            return False
        for var in assignment.keys():
            var_index = var.split(",")
            i = int(var_index[0])
            j = int(var_index[1])
            self.board[i][j] = assignment[var]
        ic(self.board)
    
    def get_partial_assignment(self):
        # checks for already assigned variables
        assignment = {} 
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != -1:
                    assignment[f"{i},{j}"] = self.board[i][j]
        return assignment    
           
    def run(self):
        partial_assignment = self.get_partial_assignment()
        assignment = self.backtracking_search(assigment=partial_assignment)
        self.print_final_board(assignment=assignment)
  
# empty sudoku board      
sudoku_board = [[-1 for _ in range(9)] for _ in range(9)]

# a general sudoku example
sudoku_board2 = [
    [5, 3, -1, -1, 7, -1, -1, -1, -1],
    [6, -1, -1, 1, 9, 5, -1, -1, -1],
    [-1, 9, 8, -1, -1, -1, -1, 6, -1],
    [8, -1, -1, -1, 6, -1, -1, -1, 3],
    [4, -1, -1, 8, -1, 3, -1, -1, 1],
    [7, -1, -1, -1, 2, -1, -1, -1, 6],
    [-1, 6, -1, -1, -1, -1, 2, 8, -1],
    [-1, -1, -1, 4, 1, 9, -1, -1, 5],
    [-1, -1, -1, -1, 8, -1, -1, 7, 9]
]


# hard level
sudoku_board3 = [
    [-1, -1, 6, 3, -1, 7, -1, -1, -1],
    [-1, -1, 4, -1, -1, -1, -1, -1, 5],
    [1, -1, -1, -1, -1, 6, -1, 8, 2],
    [2, -1, 5, -1, 3, -1, 1, -1, 6],
    [-1, -1, -1, 2, -1, -1, 3, -1, -1],
    [9, -1, -1, -1, 7, -1, -1, -1, 4],
    [-1, 5, -1, -1, -1, -1, -1, -1, -1],
    [-1, 1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 8, 1, -1, 9, -1, 4, -1]
]


#creating instance with desired board to be solved <3
sudoku = Sudoku(board=sudoku_board3)


#initializing constraints:
#GPT baram refactor karde <3:
for i in range(9):
    # Row constraints
    constraint = Constraint([f"{i},{j}" for j in range(9)])
    sudoku.add_constraint(constraint)
    # Column constraints
    constraint = Constraint([f"{j},{i}" for j in range(9)])
    sudoku.add_constraint(constraint)

# Subgrid constraints
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        constraint = Constraint([f"{i+k},{j+l}" for k in range(3) for l in range(3)])
        sudoku.add_constraint(constraint)
        
sudoku.run()
    
    