#import stats_collect
import time
import dfs
import print_graphs
import utility
from json import load

def main(variable_selection_method, inference_method):

    with open('gcp.json', 'r') as f:
        data = load(f)

    #initializing CSP parameters
    start_node = 0
    assignments = [0] * data.get('num_points')
    domains = [[1, 2, 3, 4] for i in range(data.get('num_points'))]
    constraints = utility.makeConstraints(data.get('edges'), data.get('num_points'))

    #running method and collecting time data
    t0 = time.perf_counter()
    map_color_success = dfs.backtrack(assignments, domains, constraints, start_node, variable_selection_method, inference_method)
    t1 = time.perf_counter()

    #printing visible graph and results to terminal
    points = data.get("points")
    edges = data.get("edges")
    if(map_color_success):
        print('MAP SUCCESSFULLY COLORED')
        print_graphs.print_graph1(points, edges, assignments)
        utility.print_results(inference_method, variable_selection_method, data.get('num_points'), t1-t0)
    else:
        print('FAILURE')
    


#choosing methods of CSP solver
variable_heuristics = ['sequential', 'random', 'mrv', 'mrv-degree']#possible variable heuristics
inference_algorithms = ['default', 'forward-checking', 'AC3']#possible algorithms

#to change the variable heuristic or the algorithm running, simply change the index value in the parameters below
results = main(variable_heuristics[2], inference_algorithms[1])
