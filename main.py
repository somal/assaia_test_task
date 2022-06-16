from io import visualize
from controller import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    N, M = 6, 7
    while not is_game_finished():
        visualize_field()
        request_turn()
        handle_turn()

