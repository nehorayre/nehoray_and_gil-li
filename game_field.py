import consts

def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            grid_game.append(consts.CELL_STATE[0])

    return grid_game
print(board())

def get_flag_pos():
    flag_pos = []
    for row in range(3):
        for col in range(4):
            flag_pos.append((consts.flag_row + row, consts.flag_col + col))
    return flag_pos
print(get_flag_pos())