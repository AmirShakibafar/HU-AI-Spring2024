from classes.A_star import A_star
from classes.rubicks import RubicksCube
from icecream import ic
import random


# only god knows all the suffering this caused me...
# i have solved the rubicks over 100 times for this and its still slow i dont have a brain anymore so sorry.
# dont ask how the rotations work because only god knows how...

cube = {
    "blue": ["blue" for i in range(9)],
    "green": ["green" for i in range(9)],
    "white": ["white" for i in range(9)],
    "orange": ["orange" for i in range(9)],
    "red": ["red" for i in range(9)],
    "yellow": ["yellow" for i in range(9)],
}


def shuffle_cube_random(cube, num_moves):
    moves = ["L", "L'", "R", "R'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
    moves_i_did = []
    for _ in range(num_moves):
        move = random.choice(moves)
        moves_i_did.append(move)
        if move == "L":
            cube.L_rotate()
        elif move == "L'":
            cube.L_rotate(reverse=True)
        elif move == "R":
            cube.R_rotate()
        elif move == "R'":
            cube.R_rotate(reverse=True)
        elif move == "U":
            cube.U_rotate()
        elif move == "U'":
            cube.U_rotate(reverse=True)
        elif move == "D":
            cube.D_rotate()
        elif move == "D'":
            cube.D_rotate(reverse=True)
        elif move == "F":
            cube.F_rotate()
        elif move == "F'":
            cube.F_rotate(reverse=True)
        elif move == "B":
            cube.B_rotate()
        elif move == "B'":
            cube.B_rotate(reverse=True)
            
    moves_string = " ".join(moves_i_did[::-1])
    
    return moves_string

# Example usage:
# Create a Rubik's Cube object
rubiks_cube = RubicksCube(cube)

# it gets slow after 8 moves ;(
moves = shuffle_cube_random(rubiks_cube, 6)




a_star = A_star(initial=rubiks_cube, goal=cube)
a_star.run()
ic(moves)