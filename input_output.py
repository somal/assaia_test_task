from typing import List
from controller import TurnType


def init_game():
    # TODO: add more details
    print('Welcome to the game!\n'
          'You will receive field and will make a turn as X or O\n'
          '\n'
          'Good luck!')


def visualize_field(field: List[List]):
    assert isinstance(field, list)
    assert isinstance(field[0], list)
    n, m = len(field), len(field[0])
    print('-' * (2 * m + 1))
    for row in field:
        for c in row:
            print(f'|{c.value}', end='')
        print('|')
    print('-' * (2 * m + 1))


def request_turn(turn_type: TurnType, max_columns: int) -> int:
    # TODO: add turn description
    print(f'Now is turn of {turn_type.value}')

    flag = False
    result = None
    while not flag:
        print(f'Input column number from 1 to {max_columns}:')
        i = input().strip()
        if not i.isdigit():
            print('Error: please input a number')
        else:
            i = int(i)
            if i < 1 or i > max_columns:
                print('Error: you have input wrong number')
            else:
                flag = True
                result = i
    return result
