from input_output import visualize_field, request_turn, init_game
from controller import Controller

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = (6, 7)
    cnt = Controller(size)
    init_game()
    i = 0
    while not cnt.is_game_finished():
        i += 1
        visualize_field(cnt.get_field())
        current_turn_type = cnt.get_current_turn_type()
        column_number = request_turn(current_turn_type, size[1])
        cnt.handle_turn(column_number)
        if i == 5:
            break
