import consts
import random
def board():
    grid_game = []
    for row in range(consts.BOARD_ROWS):
        for col in range(consts.BOARD_COLS):
            grid_game.append(consts.CELL_STATE[0])
    return grid_game
print(board())

def random_grass_place_x_y():
    grass_list = []
    for i in range(20):
        grass_list = [(random.randint(0,consts.WINDOW_WIDTH-40),random.randint(0,consts.WINDOW_HEIGHT-40))]
    return grass_list
