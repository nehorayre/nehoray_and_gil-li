import random
import pygame
import math
import consts
import game_field


pygame.init()

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

# -------------soldier-------------------------
def create_soldier(x,y):
    soldier_img = pygame.image.load("img/soldier.png")
    soldier_img = pygame.transform.scale(soldier_img,
                    (consts.SOLDIER_ROWS * consts.CELL_SIZE,
                     consts.SOLDIER_ROWS * consts.CELL_SIZE))
    screen.blit(soldier_img, (x, y))
    return soldier_img

def create_soldier_night(x,y):
    soldier_img = pygame.image.load("img/soldier.png")
    soldier_img = pygame.transform.scale(soldier_img,
                    (consts.SOLDIER_ROWS * consts.CELL_SIZE,
                     consts.SOLDIER_ROWS * consts.CELL_SIZE))
    screen.blit(soldier_img, (x, y))
    return soldier_img

 # ----------grass-------------
def create_grass():
    grass_img = pygame.image.load("img/grass.png")
    grass_img = pygame.transform.scale(grass_img, (consts.grass_size, consts.grass_size))
    return grass_img

def draw_random_grass():
    for i in range(20):
        temp_grass = game_field.random_x_y()[i]
        screen.blit(create_grass(), temp_grass)

# ----------------------------


# -----------boom-----------------

def create_boom():
    boom_img = pygame.image.load("img/mine.png")
    grass_img = pygame.transform.scale(boom_img,(consts.MINE_ROWS * consts.CELL_SIZE, consts.MINE_COLS * consts.CELL_SIZE))
    return grass_img

def draw_boom_by_x_y():
    count = 0
    for i in range(20):
        temp_boom = game_field.boom_list()[i]
        screen.blit(create_boom(), temp_boom)

# ----------------------------
def create_flag():
    flag_img = pygame.image.load("img/flag.png")
    flag_img = pygame.transform.scale(flag_img,(consts.FLAG_ROWS * consts.CELL_SIZE, consts.FLAG_COLS * consts.CELL_SIZE))
    screen.blit(flag_img, ((consts.flag_col * consts.CELL_SIZE) , (consts.flag_row * consts.CELL_SIZE)))
    return flag_img



# -------------message---------------
def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)


# -------------draw---------------

def draw_grid(x,y):
    create_soldier_night(x,y)
    blockSize = 20 #Set the size of the grid block
    for x in range(0, consts.WINDOW_WIDTH, blockSize):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, consts.BACKGROUND_COLOR, rect, 1)




def create_display(x,y):
    create_soldier(x, y)
    draw_random_grass()
    draw_boom_by_x_y()
    create_flag()
    pygame.display.update()