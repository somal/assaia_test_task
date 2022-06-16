from input_output import visualize_field, request_turn, init_game, celebrate_winner
from controller import Controller, TurnType

if __name__ == '__main__':
    # TODO: проверить что можно добавлять в колонку
    # TODO: add description for prints in I/O
    size = (6, 7)
    win_line_length = 4
    cnt = Controller(size, win_line_length)
    init_game()
    while cnt.get_winner() is None:
        visualize_field(cnt.get_field())
        current_turn_type = cnt.get_current_turn_type()  # type: TurnType
        column_number = request_turn(current_turn_type, size[1])  # type: int
        cnt.handle_turn(column_number, current_turn_type)

    visualize_field(cnt.get_field())
    celebrate_winner(cnt.get_winner())
