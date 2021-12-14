#the driver code is at the bottom of this document
from time import perf_counter
import file_io
import utility
import dfs

BOARD_SIZE = 3

def main(var_method, inf_method, num_empty_squares = 15):    

    #create an unsolved board
    unsolved_board = file_io.make_board(3, num_empty_squares, 'sudoku.json')
        # use the below function for getting sudoku values from a file in the dir named 'sudoku.json' (strictly unnecessary)
        # unsolved_board = file_io.get_sudoku_from_file('sudoku.json')


    #print unsolved sudoku board
    print('''
Sudoku board before DFS: 
    ''')
    utility.print_sudoku(unsolved_board, BOARD_SIZE)

    #initialize CSP 
    assignments = []
    for i in unsolved_board:
        assignments.extend(i)
    domains = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(BOARD_SIZE**4)]
    constraints = utility.get_sudoku_constraints()
    first_var = assignments.index(0)


    #run the backtracker and collect time data
    t0 = perf_counter()
    result = dfs.backtrack(assignments, domains, constraints, first_var, var_method, inf_method)
    t1 = perf_counter()
    solved_board = utility.assignments_to_sudoku_list(assignments)
    
    #print the solved sudoku board and the time taken in seconds
    print('''
Sudoku board after DFS:
    ''')
    utility.print_sudoku(solved_board, BOARD_SIZE)
    if(result):
        print('SOLVED SUCCESSFULLY')
    else:
        print('FAILURE')
    utility.print_results(inf_method, var_method, num_empty_squares, t1-t0)

    

###DRIVER CODE
variable_heuristics = ['sequential', 'random', 'mrv', 'mrv-degree']#possible variable heuristics
inference_algorithms = ['default', 'forward-checking', 'AC3']#possible algorithms
num_empty_squares = 50     #number of empty squares to initialize problem with

#to change the variable heuristics or algorithm running, just change the index in the parameters below
main(variable_heuristics[2], inference_algorithms[1], num_empty_squares)
