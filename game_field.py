import consts
import random

def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        grid_game.append([])
        for col in range(consts.BOARD_COLS):
            grid_game[row].append(consts.CELL_STATE[0])

    return grid_game

def get_flag_pos():
    flag_pos = []
    for row in range(3):
        for col in range(4):
            flag_pos.append((consts.flag_row + row, consts.flag_col + col))
            grid[consts.flag_row + row][consts.flag_col + col] = consts.CELL_STATE[2]
    return flag_pos


def add_boom_grid():
    boom_lst = []
    for i in range(20):
        row = random.randint(0, consts.BOARD_ROWS - 2)
        col =  random.randint(0, consts.BOARD_COLS)
        boom_lst.append((row, col))

        grid[row][col] = consts.CELL_STATE[1]
        grid[row][col + 1] = consts.CELL_STATE[1]
        grid[row][col + 2] = consts.CELL_STATE[1]


def random_x_y():
    lst = []
    for i in range(20):
        lst = [(random.randint(0,consts.WINDOW_WIDTH-40),random.randint(0,consts.WINDOW_HEIGHT-40))]
    return lst

gras_list = []
def random_x_y_for_gras():
    for i in range(20):
        x = random.randint(0, consts.WINDOW_WIDTH - 40)
        y = random.randint(0, consts.WINDOW_HEIGHT - 40)
        while ( x<= consts.CELL_SIZE*consts.SOLDIER_COLS and y <= consts.CELL_SIZE*consts.SOLDIER_ROWS) or (( x<= consts.CELL_SIZE*consts.FLAG_COLS- 40 and y <= consts.CELL_SIZE*consts.FLAG_ROWS)) :
            x = random.randint(0, consts.WINDOW_WIDTH - 40)
            y = random.randint(0, consts.WINDOW_HEIGHT - 40)
        gras_list.append((x,y))
    return gras_list

grid = board()
get_flag_pos()
add_boom_grid()
