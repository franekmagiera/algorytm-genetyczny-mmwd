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
            transport_cost = transport_cost_matrix[solution[i], solution[j]] + transport_cost_matrix[solution[j], solution[i]]
            # distance = abs(row_j - row_i) + abs(column_j - column_i) # odkomentowac jesli nie bedziemy korzystac z macierzy odleglosci
            distance = distance_matrix[i, j]
            value += transport_cost * distance 
    return value/2  # aktualnie badamy jedynie symetryczne macierze kosztow


def fit_fun(solution):
    return fitness_function(solution, transport_cost_matrix, distance_matrix)

#OPTIMAL SOLUTION
#sol = [34,4,5,11,10,26,25,24,23,8,3,0,12,19,13,22,20,21,1,7,9,6,27,18,31,33,32,16,17,2,14,15,28,29,30,35]
#print(fit_fun(sol))
