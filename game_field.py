import consts

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

def get_boom_list_pos():
    boom_list = []

def print_lst(lst):
    for row in lst:
        for col in row:
            print(str(col), end=" ")
        print()

grid = board()
get_flag_pos()
print_lst(grid)