from enum import Enum
from typing import Tuple


class TurnType(Enum):
    X = 'X'
    O = 'O'
    Nan = '_'


class Controller(object):
    def __init__(self, size: Tuple[int, int], win_line_length: int):
        assert isinstance(size, tuple)
        assert len(size) == 2
        assert size[0] > 0 and size[1] > 0
        assert win_line_length > 0

        self._size = size
        self._field = [[TurnType.Nan for _ in range(size[1])] for _ in range(size[0])]
        self._win_line_length = win_line_length

        self._turns_number = -1
        self._winner = None

    def get_current_turn_type(self) -> TurnType:
        self._turns_number += 1
        return list(TurnType)[self._turns_number % (len(TurnType) - 1)]

    def is_game_finished(self) -> bool:
        return self._winner is not None

    def handle_turn(self, column_number: int, turn_type: TurnType):
        for row_ind in range(self._size[0] - 1, -1, -1):
            if self._field[row_ind][column_number - 1] is TurnType.Nan:
                self._field[row_ind][column_number - 1] = turn_type
                break
        self.check_field()

    # TODO: implement
    def check_field(self):
        pass

    def get_field(self):
        return self._field
