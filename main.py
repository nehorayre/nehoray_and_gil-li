import consts
import screen

state = {
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
    "visual_state": consts.NORMAL_VISION,
    "soldier_direction": consts.NOT_MOVING
}


def main():
    screen.draw_grid(0,0)
    screen.draw_xray()

if __name__ == "__main__":
    while True:
        main()