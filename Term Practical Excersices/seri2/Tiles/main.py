from classes.a_star import A_star
from classes.tiles_game import Tiles_game
         

            
initial = [[0, 1, 0, 0],
           [1, 2, 3, 4],
           [0, 4, 0, 0],
           [0, 3, 1, 0]]

goal = [[3, 1, 4, 1],
        [0, 0, 3, 1],
        [0, 0, 0, 2],
        [0, 0, 0, 4]]

tiles = Tiles_game(w=4, h=4, g=0, board=initial)
a_star = A_star(initial=tiles, goal=goal)
a_star.run()