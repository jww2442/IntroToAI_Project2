
'''inputs sudoku list
inputs board_size: length of the small boxes in a sudoku board (if ==3, then board is a 9x9)
prints that list to the console
outputs nothing'''
def print_sudoku(sudoku_list, board_size):

    print('-------------------------')
    for i, li in enumerate(sudoku_list):

        print('| ', end='')
        for j, num in enumerate(li):
            print(num, '', end='')
            if((j+1)%board_size == 0):
                print('| ', end='')
        print('')
        if((i+1)%board_size == 0): 
            print('-------------------------')

def assignments_to_sudoku_list(assignments):
    sud_list = []
    for i in range(9):
        inner = []
        for j in range(9):
            inner.append(assignments[i*9 + j])
        sud_list.append(inner)
    return sud_list
    
def print_results(inftype, varseltype, numnodes, time):
    algotype = ''
    if(inftype == 'default'):
        algotype = 'DFS with backtracking only'
    elif(inftype == 'forward-checking'):
        algotype = 'DFS with backtracking and forward checking'
    elif(inftype == 'AC3'):
        algotype = 'DFS with backtracking and AC3'
    else: 
        print('err 851')
    
    print('Algorithm type:              \t*', algotype, '*\nVariable selection heuristic:\t*', varseltype, '*\nNumber of empty squares:     \t*', numnodes, '*\nAlgorithm time in seconds:   \t*', time, '*\n')

def get_var_num(col, row):
    return row*9 + col

def get_sudoku_constraints():
    c = [set() for i in range(81)]

    for i in range(81):

        row = (i)//9
        col = i%9
        for j in range(row*9, row*9 + 9):
            c[i].add(j)
        for k in range(9):
            c[i].add(k*9 + col)
        r3 = row % 3
        c3 = col % 3

        if(r3 == 0 and c3 == 0): 
            c[i].add(get_var_num(col+1, row + 1))
            c[i].add(get_var_num(col+1, row + 2))
            c[i].add(get_var_num(col+2, row + 1))
            c[i].add(get_var_num(col+2, row + 2))
        elif(r3 == 1 and c3 == 0):
            c[i].add(get_var_num(col+1, row - 1))
            c[i].add(get_var_num(col+1, row + 1))
            c[i].add(get_var_num(col+2, row - 1))
            c[i].add(get_var_num(col+2, row + 1))
        elif(r3 == 2 and c3 == 0):
            c[i].add(get_var_num(col+1, row - 2))
            c[i].add(get_var_num(col+1, row - 1))
            c[i].add(get_var_num(col+2, row - 2))
            c[i].add(get_var_num(col+2, row - 1))
        elif(r3 == 0 and c3 == 1):
            c[i].add(get_var_num(col-1, row + 1))
            c[i].add(get_var_num(col-1, row + 2))
            c[i].add(get_var_num(col+1, row + 1))
            c[i].add(get_var_num(col+1, row + 2))
        elif(r3 == 1 and c3 == 1):
            c[i].add(get_var_num(col+1, row + 1))
            c[i].add(get_var_num(col-1, row + 1))
            c[i].add(get_var_num(col+1, row - 1))
            c[i].add(get_var_num(col-1, row - 1))
        elif(r3 == 2 and c3 == 1):
            c[i].add(get_var_num(col-1, row - 2))
            c[i].add(get_var_num(col-1, row - 1))
            c[i].add(get_var_num(col+1, row - 1))
            c[i].add(get_var_num(col+1, row - 2))
        elif(r3 == 0 and c3 == 2):
            c[i].add(get_var_num(col-2, row + 1))
            c[i].add(get_var_num(col-2, row + 2))
            c[i].add(get_var_num(col-1, row + 1))
            c[i].add(get_var_num(col-1, row + 2))
        elif(r3 == 1 and c3 == 2):
            c[i].add(get_var_num(col-2, row - 1))
            c[i].add(get_var_num(col-1, row - 1))
            c[i].add(get_var_num(col-2, row + 1))
            c[i].add(get_var_num(col-1, row + 1))
        elif(r3 == 2 and c3 == 2):
            c[i].add(get_var_num(col-2, row - 2))
            c[i].add(get_var_num(col-1, row - 2))
            c[i].add(get_var_num(col-2, row - 1))
            c[i].add(get_var_num(col-1, row - 1))

    constraints = []
    for i, num_set in enumerate(c):
        constraints.append(list(num_set))
        constraints[i].remove(i)#?
    return constraints
    