import matplotlib.pyplot as plt
import networkx as nx
from ortools.linear_solver import pywraplp

def get_rr_solver(G, number_of_nodes):

    solver = pywraplp.Solver.CreateSolver('SAT')
    
    y = [solver.IntVar(0.0, 1.0, 'y{}'.format(i)) for i in range(number_of_nodes)]
    x = [solver.IntVar(0.0, 1.0, 'x{}'.format(i)) for i in range(number_of_nodes)]
    
    solver.Minimize(solver.Sum(x[i]+y[i] for i in range(number_of_nodes)))

    for i in range(number_of_nodes):
        print(type(x[i]))

    return solver

get_rr_solver("", 5)
