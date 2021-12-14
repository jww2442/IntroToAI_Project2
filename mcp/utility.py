

'''input edges list and num of nodes, 
output constraint list where each index i contains a set of all the nodes that have edges connected to node i'''
def makeConstraints(edges, numNodes):

    #initializes constraints list to as many sets as num of nodes
    constraints=[set() for k in range(numNodes)]

    for e in edges:
        constraints[e[0]].add(e[1])
        constraints[e[1]].add(e[0])

    for s in range(len(constraints)):
        constraints[s] = list(constraints[s])
    return list(constraints)


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
    
    print('Algorithm type:              \t*', algotype, '*\nVariable selection heuristic:\t*', varseltype, '*\nNumber of nodes:             \t*', numnodes, '*\n----------------------------------------------------\nTime in seconds:             \t*', time, '*\n')

def print_stats(inftype, varseltype, numnodes, stats):

    sum = 0
    for t in stats: 
        sum += t
    average = sum / len(stats)

    if(inftype == 'default'):
        algotype = 'DFS with backtracking only'
    elif(inftype == 'forward-checking'):
        algotype = 'DFS with backtracking and forward checking'
    elif(inftype == 'AC3'):
        algotype = 'DFS with backtracking and AC3'
    else: 
        print('err 852')
    
    print('# of Prob instances:        \t*', len(stats), '*\nAlgorithm type:              \t*', algotype, '*\nVariable selection heuristic:\t*', varseltype, '*\nNumber of nodes:             \t*', numnodes, '*\n----------------------------------------------------\nAverage time in seconds:     \t*', average, '*\n')

