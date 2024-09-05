import matplotlib.pyplot as plt
import networkx as nx
from ortools.linear_solver import pywraplp

def generate_index_label(index):
    if (ord('a') + index <= ord('z')):
        return chr(ord('a') + index)
    elif (ord('A') + index <= ord('Z')):
        return chr(ord('A') + index)
    else:
        return 'Z' + generate_index_label(index - 50)


def get_rr_solver(G, number_of_nodes):

    solver = pywraplp.Solver.CreateSolver('SAT')
    
    y = [solver.IntVar(0.0, 1.0, 'y{}'.format(i)) for i in range(number_of_nodes)]
    x = [solver.IntVar(0.0, 1.0, 'x{}'.format(i)) for i in range(number_of_nodes)]
    
    solver.Minimize(solver.Sum(x[i]+y[i] for i in range(number_of_nodes)))
    
    for i in range(number_of_nodes):
        solver.Add(x[i] + solver.Sum(y[j[1]] for j in G.edges(i)) >= 1)
    
    for i in range(number_of_nodes):
        solver.Add(y[i] <= x[i])

    return solver


def get_graphs_infos(size_variable):
    infos = []

    default_number_of_nodes = int(10**size_variable)
    size_variable = int((size_variable + 0.5) // 1) # Round it UP
    infos.append(
        {
            "G" : nx.complete_graph(default_number_of_nodes),
            "number_of_nodes" : default_number_of_nodes,
            "name" : "Complete"
        }
    )

    infos.append(
        {
            "G" : nx.star_graph(default_number_of_nodes-1),
            "number_of_nodes" : default_number_of_nodes,
            "name" : "Star"
        }
    )

    infos.append(
        {
            "G" : nx.cycle_graph(default_number_of_nodes),
            "number_of_nodes" : default_number_of_nodes,
            "name" : "Cycle"
        }
    )

    infos.append(
        {
            "G" : nx.path_graph(default_number_of_nodes),
            "number_of_nodes" : default_number_of_nodes,
            "name" : "Path"
        }
    )

    infos.append(
        {
            "G" : nx.binomial_tree(2*size_variable),
            "number_of_nodes" : 2**(2*size_variable),
            "name" : "Binomial Tree"
        }
    )

    for randomness in [30, 50, 80]:
        infos.append(
            {
                "G" : nx.binomial_graph(default_number_of_nodes, randomness/100),
                "number_of_nodes" : default_number_of_nodes,
                "name" : "Binomial Graph ({}%)".format(randomness)
            }
        )

    return infos

