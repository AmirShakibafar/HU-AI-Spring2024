from copy import deepcopy

class Tiles_game:
    def __init__(self, w, h, g, board, move_that_created=None, parent=None) -> None:
        self.board: list[list] = board
        self.w = w
        self.h = h
        self.g = g
        # we add h in A* 
        self.f = g
        self.next_states: list = []
        self.move_that_created = move_that_created
        self.parent = parent
    
    def heuristic(self, goal_state):
        count = 0
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] == goal_state[i][j]:
                    count += 1
        self.f += count
            
    def check_goal(self, goal_state: list):
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j] != goal_state[i][j]:
                    return False
        return True
        
    def find_bounds(self, move):
        if move == "up":
            start = 0
            step = 1
            end = self.h
            
        elif move == "down":
            start = self.h - 1
            step = -1
            end = -1
            
        elif move == "left":
            start = 0
            step = 1
            end = self.w
            
        elif move == "right":
            start = self.w - 1
            step = -1
            end = -1
            
        else:
            raise Exception("invalid move")
        
        return start,end,step
    
    def swap_in_rows(self, left: bool, board):
        
        if left:
            move = "left"
        else:
            move = "right"
         
        # find bounds based on what is the move   
        start,end,step = self.find_bounds(move)  
            
        for row in board:
            for i in range(start, end, step):
                for j in range(i, end, step):
                    if row[i] != 0:
                        break
                    if row[j] != 0:
                        row[i], row[j] = row[j], row[i]
        
        return board
                    
    def swap_in_columns(self, up: bool, board):
        
        if up:
            move = "up"
        else:
            move = "down"
         
        # find bounds based on what is the move   
        start,end,step = self.find_bounds(move)  
        
        for col in range(self.w):
            for i in range(start, end, step):
                for j in range(i, end, step):
                    if board[i][col] != 0:
                        break
                    if board[j][col] != 0:
                        board[i][col], board[j][col] = board[j][col], board[i][col]
        
        return board
                            
    def move_left(self):
        board = deepcopy(self.board)
        board = self.swap_in_rows(left=True, board=board)
        next_tiles_game = Tiles_game(w=self.w, h=self.h, g=self.g+1, board=board, move_that_created="left", parent=self)
        return next_tiles_game
        
    def move_right(self):
        board = deepcopy(self.board)
        board = self.swap_in_rows(left=False, board=board)
        next_tiles_game = Tiles_game(w=self.w, h=self.h, g=self.g+1, board=board, move_that_created="right", parent=self)
        return next_tiles_game
    
    def move_up(self):
        board = deepcopy(self.board)
        board = self.swap_in_columns(up=True, board=board)
        next_tiles_game = Tiles_game(w=self.w, h=self.h, g=self.g+1, board=board, move_that_created="up", parent=self)
        return next_tiles_game
    
    def move_down(self):
        board = deepcopy(self.board)
        board = self.swap_in_columns(up=False, board=board)
        next_tiles_game = Tiles_game(w=self.w, h=self.h, g=self.g+1, board=board, move_that_created="down", parent=self)
        return next_tiles_game
    
    def generate_next_states(self):
        self.next_states.append(self.move_left())
        self.next_states.append(self.move_right())
        self.next_states.append(self.move_up())
        self.next_states.append(self.move_down())
    
    def generate_string_version(self):
        result = ""
        for row in self.board:
            result += " ".join(map(str, row)) + "\n"
        return result   