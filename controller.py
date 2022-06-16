from enum import Enum
from typing import Tuple, List, Union


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

    def get_winner(self) -> TurnType:
        return self._winner

    def handle_turn(self, column_number: int, turn_type: TurnType):
        for row_ind in range(self._size[0] - 1, -1, -1):
            if self._field[row_ind][column_number - 1] is TurnType.Nan:
                self._field[row_ind][column_number - 1] = turn_type
                break
        self.check_field()

    def check_field(self):
        directions = ((-1, 0), (0, -1), (-1, -1), (-1, 1))
        for i in range(self._size[0]):
            for j in range(self._size[1]):
                for dir in directions:
                    line = self._get_line(i, j, dir)
                    if line is not None:
                        for turn_type in list(TurnType)[:-1]:
                            flag = True
                            for item in line:
                                if item != turn_type:
                                    flag = False
                                    break
                            if flag:
                                # print(line, turn_type, i, j, dir)
                                self._winner = turn_type

    def _get_line(self, i: int, j: int, direction: Tuple[int, int]) -> Union[None, List[TurnType]]:
        line = [self._field[i][j]]
        for _ in range(self._win_line_length - 1):
            i += direction[0]
            j += direction[1]
            if i < 0 or j < 0 or i >= self._size[0] or j >= self._size[1]:
                return None
            else:
                line.append(self._field[i][j])
        return line

    def get_field(self):
        return self._field
