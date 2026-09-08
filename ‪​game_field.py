import consts

def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            grid_game.append(consts.CELL_STATE[0])

    return grid_game
print(board())
