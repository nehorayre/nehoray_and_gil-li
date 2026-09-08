import consts
import game_field

def init_soldier():
    return {
        "left_up_x" : 0,
        "left_up_y" : 0,
    }

def get_soldier_leg_pos(left_up_x, left_up_y):
    return [(left_up_x, left_up_y + 3), (left_up_x + 1, left_up_y + 3)]

def get_soldier_body(left_up_x, left_up_y):
    return [(left_up_x, left_up_y), (left_up_x, left_up_y + 1),
            (left_up_x + 1, left_up_y + 2), (left_up_x + 1, left_up_y),
            (left_up_x + 1, left_up_y + 1), (left_up_x + 1, left_up_y + 2)]

def is_touching_boom(boom_pos):
    for leg in range(len(soldier_legs)):
        if soldier_legs[leg] in boom_pos:
            return True
    return False

def is_touching_flag():
    flag_pos = game_field.get_flag_pos()
    for body in range(len(soldier_legs)):
        if soldier_legs[body] in flag_pos:
            return True
    return False

def is_inside_border():
    for body in range(len(soldier_full_body)):
        if soldier_full_body[body][0] < 0 or soldier_full_body[body][0] > consts.BOARD_ROWS:
            if soldier_full_body[body][1] < 0 or soldier_full_body[body][1] > consts.BOARD_COLS:
                return False
    return True


soldier = init_soldier()
soldier_legs = get_soldier_leg_pos(soldier["left_up_x"], soldier["left_up_y"])
soldier_body = get_soldier_body(soldier["left_up_x"], soldier["left_up_y"])
soldier_full_body = soldier_body + soldier_legs
