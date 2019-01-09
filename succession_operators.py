from fitness_function import fitness_function
from read_config import transport_cost_matrix, distance_matrix
import numpy as np
import random


def fit_fun(solution):
    return fitness_function(solution, transport_cost_matrix, distance_matrix)


def children_only(size, children, parents):
    children.sort(key=fit_fun)
    population = children[:size][:]
    return population


def mixed(size, children, parents):
    population = np.vstack((children, parents))
    random.shuffle(population)
    return population[:size]

