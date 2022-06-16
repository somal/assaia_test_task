from input_output import visualize_field, request_turn
from controller import Controller

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = (6, 7)
    cnt = Controller(size)
    while not cnt.is_game_finished():
        visualize_field(cnt.get_field())
        request_turn()
        cnt.handle_turn(0)
        break
