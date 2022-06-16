from enum import Enum
from typing import Tuple


class TurnType(Enum):
    X = 'X'
    O = 'O'
    Nan = '_'


class Controller(object):  # TODO: make Singleton
    def __init__(self, size: Tuple[int, int]):
        assert isinstance(size, tuple)
        assert len(size) == 2
        assert size[0] > 0 and size[1] > 0

        self._field = [[TurnType.Nan] * size[1]] * size[0]
        self._turns_number = -1

    def get_current_turn_type(self) -> TurnType:
        self._turns_number += 1
        return list(TurnType)[self._turns_number % (len(TurnType) - 1)]

    # TODO: implement
    def is_game_finished(self) -> bool:
        return False

    # TODO: implement
    def handle_turn(self, column_number: int):
        pass

    def get_field(self):
        return self._field
