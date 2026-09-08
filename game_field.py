import consts

import random
def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        grid_game.append([])
        for col in range(consts.BOARD_COLS):
            grid_game[row].append(consts.CELL_STATE[0])

            grid_game.append(consts.CELL_STATE[0])
    return grid_game
print(board())

def get_flag_pos():
    flag_pos = []
    for row in range(3):
        for col in range(4):
            flag_pos.append((consts.flag_row + row, consts.flag_col + col))
            grid[consts.flag_row + row][consts.flag_col + col] = consts.CELL_STATE[2]
    return flag_pos

def get_boom_list_pos():
    boom_list = []
def random_grass_place_x_y():
    grass_list = []
    for i in range(20):
        grass_list = [(random.randint(0,consts.WINDOW_WIDTH-40),random.randint(0,consts.WINDOW_HEIGHT-40))]
    return grass_list

def print_lst(lst):
    for row in lst:
        for col in row:
            print(str(col), end=" ")
        print()

grid = board()
get_flag_pos()
print_lst(grid)