from typing import List


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


def request_turn():
    pass
