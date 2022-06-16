from input_output import visualize_field, request_turn, init_game
from controller import Controller, TurnType

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # TODO: проверить что можно добавлять в колонку
    # TODO: make Singleton for Controller
    # TODO: add description for prints in I/O
    size = (6, 7)
    win_line_length = 5
    cnt = Controller(size, win_line_length)
    init_game()
    i = 0
    while not cnt.is_game_finished():
        i += 1
        visualize_field(cnt.get_field())
        current_turn_type = cnt.get_current_turn_type()  # type: TurnType
        column_number = request_turn(current_turn_type, size[1])  # type: int
        cnt.handle_turn(column_number, current_turn_type)
        if i == 5:
            break
