import consts
import screen
import pygame
import soldier
import time

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "visual_state": consts.NORMAL_VISION,
    "x_ray_time" : time.time(),
    "soldier_direction": consts.NOT_MOVING
}

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["state"] = consts.LOSING_STATE

        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                soldier.move_down()
                screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
                state["soldier_direction"] = consts.DOWN

            elif event.key == pygame.K_UP:
                soldier.move_up()
                screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
                state["soldier_direction"] = consts.UP

            elif event.key == pygame.K_RIGHT:
                soldier.move_right()
                screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
                state["soldier_direction"] = consts.RIGHT

            elif event.key == pygame.K_LEFT:
                soldier.move_left()
                screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
                state["soldier_direction"] = consts.LEFT

            elif event.key == pygame.K_RETURN:
                screen.draw_grid_xray(soldier.get_pos()[0], soldier.get_pos()[1])
                state["visual_state"] = consts.X_RAY_VISION
                state["soldier_direction"] = consts.NOT_MOVING
                state["x_ray_time"] = time.time() - state["x_ray_time"]

def main():
    pygame.init()

    while True:
        screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
        if state["visual_state"] == consts.X_RAY_VISION:
            if  time.time() - state["x_ray_time"] > 3:
                screen.draw_grid_normal(soldier.get_pos()[0], soldier.get_pos()[1])
                state["visual_state"] = consts.NORMAL_VISION

        handle_user_events()

if __name__ == "__main__":
    main()