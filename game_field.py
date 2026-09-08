import consts
import random
def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            grid_game.append(consts.CELL_STATE[0])
    return grid_game
print(board())

gras_list = []
def random_x_y():
    for i in range(20):
        x = random.randint(0, consts.WINDOW_WIDTH - 40)
        y = random.randint(0, consts.WINDOW_HEIGHT - 40)
        while ( x<= consts.CELL_SIZE*consts.SOLDIER_COLS and y <= consts.CELL_SIZE*consts.SOLDIER_ROWS) or (( x<= consts.CELL_SIZE*consts.FLAG_COLS- 40 and y <= consts.CELL_SIZE*consts.FLAG_ROWS)) :
            x = random.randint(0, consts.WINDOW_WIDTH - 40)
            y = random.randint(0, consts.WINDOW_HEIGHT - 40)
        gras_list.append((x,y))
    return gras_list