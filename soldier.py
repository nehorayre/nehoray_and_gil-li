import consts
import game_field

def init_soldier(x = 0, y = 0):
    return {
        "left_up_x" : x,
        "left_up_y" : y,
    }

def get_soldier_leg_pos(left_up_x, left_up_y):
    return [(left_up_x, left_up_y + 3), (left_up_x + 1, left_up_y + 3)]

def get_soldier_body(left_up_x, left_up_y):
    return [(left_up_x, left_up_y), (left_up_x, left_up_y + 1),
            (left_up_x + 1, left_up_y + 2), (left_up_x + 1, left_up_y),
            (left_up_x + 1, left_up_y + 1), (left_up_x + 1, left_up_y + 2)]

global soldier
soldier = init_soldier()
soldier_legs = get_soldier_leg_pos(soldier["left_up_x"], soldier["left_up_y"])
soldier_body = get_soldier_body(soldier["left_up_x"], soldier["left_up_y"])
soldier_full_body = soldier_body + soldier_legs

def is_touching_boom():
    mine_lst = game_field.add_mine_to_grid()
    for index in range(len(soldier_legs)):
        if (soldier_legs[index][1], soldier_legs[index][0]) in mine_lst:
            return True
    return False

def is_touching_flag():
    flag_pos = game_field.get_flag_pos()

    for body in range(len(soldier_legs)):
        if (soldier_body[body][1], soldier_body[body][0]) in flag_pos:
            return True
    return False

def is_inside_border():
    for body in range(len(soldier_full_body)):
        if soldier_full_body[body][1] < 0 or soldier_full_body[body][1] > consts.BOARD_ROWS:
            if soldier_full_body[body][0] < 0 or soldier_full_body[body][0] > consts.BOARD_COLS:
                return False
    return True

def move_up():
    if is_inside_border():
        soldier["left_up_y"] -= 1
        update_poses()

def move_down():
    if is_inside_border():
        soldier["left_up_y"] += 1
        update_poses()

def move_left():
    if is_inside_border():
        soldier["left_up_x"] -= 1
        update_poses()

def move_right():
    if is_inside_border():
        soldier["left_up_x"] += 1
        update_poses()

def get_pos():
    return (soldier["left_up_x"], soldier["left_up_y"])

def update_poses():
    global soldier, soldier_body, soldier_legs
    soldier_legs = get_soldier_leg_pos(soldier["left_up_x"],soldier["left_up_y"])
    soldier_body = get_soldier_body(soldier["left_up_x"], soldier["left_up_y"])

