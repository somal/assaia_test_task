from typing import List
from controller import TurnType


def init_game():
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


def request_turn(turn_type: TurnType, max_columns: int, unavailable_columns: List[int]) -> int:
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
            elif i in unavailable_columns:
                print('This column is busy. Please select another')
            else:
                flag = True
                result = i
    return result


def celebrate_winner(winner: TurnType):
    print(f'Oh! {winner.value} wins!')
    print('Celebration!')
