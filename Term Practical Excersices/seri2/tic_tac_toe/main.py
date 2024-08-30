board_size = 3

reward = 10

class XO:
    def __init__(self, board) -> None:
        self.board = board
        self.computer = "X"
        self.player = "O"
    
    def run(self):
        while True:
            first_or_sec = input("who playes first? (C)omptuer or (Y)ou   ")
            first_or_sec = first_or_sec.capitalize()
            if first_or_sec == "Y":
                
                while True:
                    self.print_board()
                    self.player_move()
                    self.computer_move()
            elif first_or_sec == "C":
                
                while True:
                    self.computer_move()
                    self.print_board()
                    self.player_move()
            else:
                
                print(f"invalid input: {first_or_sec}")
            
    def print_board(self):
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-+-+-")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-+-+-")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("\n")
    
    def pos_is_empty(self, position):
        if self.board[position] == " ":
            return True
        return False
        
    def update_player_position(self, player, position):
        if self.pos_is_empty(position):
            self.board[position] = player
            self.check_game_state()
        else:
            print("you cant play here!")
            self.player_move()
    
    def is_draw(self):
        for pos in self.board.keys():
            if self.board[pos] == " ":
                return False
        return True
    
    def is_winning(self, player):
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True
        
        for i in range(1, 8, 3):
            if self.board[i] == player and self.board[i + 1] == player and self.board[i + 2] == player:
                return True
        
        for i in range(1, 4):
            if self.board[i] == player and self.board[i + 3] == player and self.board[i + 6] == player:
                return True
        
        return False   
                
    def check_game_state(self):
        
        if self.is_draw():  
            self.print_board()          
            print("Draw!")
            exit()
            
        if self.is_winning(self.player):
            self.print_board()
            print("player wins!")
            exit()
        
        if self.is_winning(self.computer):
            self.print_board()
            print("computer wins!")
            exit()
            
    def player_move(self):
        position = int(input("=>"))
        self.update_player_position(self.player, position)
        
    def computer_move(self):
        best_score = -float('inf')
        
        best_move = 0   
        
        for position in self.board.keys():
            if self.board[position] == " ":
                self.board[position] = self.computer
                score = self.minimax(0, -float('inf'), float('inf'), False)
                self.board[position] = " "
                
                if score > best_score:
                    best_score = score
                    best_move = position
                    
        self.board[best_move] = self.computer
        self.check_game_state()
         
    def minimax(self, depth, alpha, beta, is_maximizer):
        if self.is_winning(player=self.computer):
            return reward 
        
        if self.is_winning(player=self.player):
            return -reward
        
        if self.is_draw():
            return 0
        
        if is_maximizer:
            best_score = -float('inf')
            for position in self.board.keys():
                if self.board[position] == " ":
                    self.board[position] = self.computer
                    score = self.minimax(depth + 1, alpha, beta, False)
                    self.board[position] = " "
                
                    if score > best_score:
                        best_score = score
                    
                    alpha = max(alpha, score)
                    
                    if alpha >= beta:
                        break
            
            return best_score
        
        else:
            best_score = float('inf')
            for position in self.board.keys():
                if self.board[position] == " ":
                    
                    self.board[position] = self.player
                    score = self.minimax(depth + 1, alpha, beta, True)
                    self.board[position] = " "
                    
                    if score < best_score:
                        best_score = score
                        
                    beta = min(beta, score)
                    
                    if alpha >= beta: 
                        break 
            
            return best_score
            
            
        
        
        
board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}    
 
xo = XO(board=board)
xo.run()