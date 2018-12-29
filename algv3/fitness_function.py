import numpy as np
from read_config import transport_cost_matrix, distance_matrix


def fitness_function(solution, transport_cost_matrix, distance_matrix):
    value = 0
    rows = np.size(transport_cost_matrix, 0)
    columns = np.size(transport_cost_matrix, 1)
    for i in range(len(solution)):
        for j in range(len(solution)):
            # row_i = i // columns
            # column_i = i % columns
            # row_j = j // columns
            # column_j = j % columns
            transport_cost = transport_cost_matrix[solution[i], solution[j]] # + transport_cost_matrix[solution[j], solution[i]]
            # distance = abs(row_j - row_i) + abs(column_j - column_i) # odkomentowac jesli nie bedziemy korzystac z macierzy odleglosci
            distance = distance_matrix[i, j]
            value += transport_cost * distance 
    return value/2 # aktualnie badamy jedynie symetryczne macierze kosztow


def fit_fun(solution):
    return fitness_function(solution, transport_cost_matrix, distance_matrix)
