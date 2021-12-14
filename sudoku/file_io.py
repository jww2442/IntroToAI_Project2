import os
import sudoku_generator as sg
from random import sample, shuffle
from json import dumps

'''creates sudoku file by running commands on the terminal
!!! this method is now deprecated by the 'make_board' method'''
def cmd_create_file(num_empty):
    command = 'python .\sudoku-generator.py ' + str(num_empty)
    os.system(command)


'''makes a random sudoku board with the suggested block_size, num of missing squares, and name for the output file'''
def make_board(block_size, num_missing, output_file):
    board = _make_board(block_size)

    ms = int(pow(block_size, 2))
    indices = sample(list(range(ms * ms)), num_missing)
    for index in indices:
        r = int(index / ms)
        c = int(index % ms)
        board[r][c] = 0

    ## Write to file
    with open(output_file, 'w') as f:
        f.write(dumps(board))

    return board


'''inputs path to sudoku txt file 
outputs data from file in list'''
def get_sudoku_from_file(file_path):

    #makes string from file contents
    with open(file_path) as f:
        str_f_contents = f.read()

    #makes list from file contents
    li_f_contents = eval(str_f_contents)

    return li_f_contents


'''from sudoku-generator.py file given to us'''
def _make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()