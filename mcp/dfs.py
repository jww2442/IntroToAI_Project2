from sys import exit
from random import choice
import numpy as np
from collections import deque

def backtrack(assignments, domains, constraints, variable, var_selection_method, inference_method):
    if(not 0 in assignments):
        return True
    
    for poss_val in domains[variable]:
        if(_val_consistent(poss_val, assignments, constraints[variable])):

            assignments[variable] = poss_val
            
            changes = _alter_domain(variable, poss_val, assignments, domains, constraints,inference_method)

            if(not changes == [-1]):#if inferences succeeds
                next_var = _choose_next_var(assignments, domains, constraints, var_selection_method)

                result = backtrack(assignments, domains, constraints, next_var, var_selection_method, inference_method)

                if(result):
                    return True
                
                _undo_changes(changes, domains)

            assignments[variable] = 0

    return False




def _choose_next_var(assignments, domains, constraints, var_selection_method):

    if(var_selection_method == 'sequential'):
        if(0 in assignments):
            return assignments.index(0)
        return -1 #shouldn't matter if all vars are assigned
    elif(var_selection_method == 'random'):
        options = []
        for i in range(len(assignments)):
            if(assignments[i] == 0):
                options.append(i)
        if(len(options) == 0):
            return -1 #doesnt matter what (?)
        return choice(options)

    elif(var_selection_method == 'mrv'): #choose the variable with the fewest values in domain
        options = []
        for i in range(len(assignments)):
            if(assignments[i] == 0):
                options.append(i)
        
        smallest_domain_size = np.inf
        smallest_dom_ind = -1
        for i in options:
            if(len(domains[i])<smallest_domain_size):
                smallest_domain_size = len(domains[i])
                smallest_dom_ind = i
        return smallest_dom_ind

    elif(var_selection_method == 'mrv-degree'):
        options = []
        for i in range(len(assignments)):
            if(assignments[i] == 0):
                options.append(i)
        
        smallest_domain_size = np.inf
        for i in options:
            if(len(domains[i])<smallest_domain_size):
                smallest_domain_size = len(domains[i])

        options2 = []
        for i in options:
            if(len(domains[i]) == smallest_domain_size):
                options2.append(i)
        
        most_constraints_num = -np.inf
        most_con_ind = -1
        for i in options2:#cons on unassigned
            cons = __constraints_on_unassigned(constraints[i], assignments)
            if(cons>most_constraints_num):
                most_constraints_num = cons
                most_con_ind = i
        return most_con_ind

    else: 
        exit('error 103')

def _undo_changes(dchanges, domains):
    for var_changed in dchanges:
        domains[var_changed[0]].extend(var_changed[1])
        domains[var_changed[0]].sort()

def _alter_domain(var, val, assignments, domains, constraints, inference_method):
    if(inference_method == 'default'):
        return []
    elif(inference_method == 'forward-checking'):
        #values elim-ed from domain of var
        changes = [[var, []]]
        for dvalue in domains[var]:
            if(not dvalue == val):
                changes[0][1].append(dvalue)
        for cvalue in changes[0][1]:
            domains[var].remove(cvalue)
        
        #values elimed from domains of var's constraints
        for con in constraints[var]:
            if(val in domains[con]):
                changes.append([con, [val]])
                domains[con].remove(val)
        
        if(not [] in domains):
            return changes
        else:
            _undo_changes(changes, domains)
            return [-1]
            
    elif(inference_method == 'AC3'):
        #values elim-ed from domain of var
        changes = [[var, []]]
        for dvalue in domains[var]:
            if(not dvalue == val):
                changes[0][1].append(dvalue)
        for cvalue in changes[0][1]:
            domains[var].remove(cvalue)

        #setting up queue
        arcs = deque()
        for con in constraints[var]:
            if(assignments[con] == 0):
                arcs.appendleft((con, var))
        
        #AC3 algorithm
        while(not len(arcs) == 0):
            (i, j) = arcs.pop()
            temp_changes = __revise(domains, (i, j))
            if(not temp_changes == [-1]): #if revision happened
                changes.extend(temp_changes)
                if(len(domains[i]) == 0):
                    _undo_changes(changes, domains)#is this modular enough? 
                    return [-1]
                for neighbor in constraints[i]:
                    if(not neighbor == j):
                        arcs.appendleft((neighbor, i))

        return changes
    
def __revise(domains, tup):
    revised = False
    internal_changes = []
    for x in domains[tup[0]]:
        con_satisfied = False
        for y in domains[tup[1]]:
            if(not x == y):
                con_satisfied = True
        if(not con_satisfied):
            domains[tup[0]].remove(x)
            internal_changes.append([tup[0], [x]])
            revised = True
    if(revised):
        return internal_changes
    else: 
        return [-1]

def _val_consistent(val, assignments, var_constraints): 

    for con in var_constraints:
        if(assignments[con] == val): 
            return False
    
    return True

def __constraints_on_unassigned(var_constraints, assignments):
    num_cons_on_unassigned = 0
    for con in var_constraints:
        if(assignments[con] == 0):
            num_cons_on_unassigned += 1
    return num_cons_on_unassigned
