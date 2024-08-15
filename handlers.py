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

    infos.append(
        {
            "G" : nx.complete_graph(number_of_nodes),
            "number_of_nodes" : 10**size_variable,
            "name" : "complete"
        }
    )
    return infos
