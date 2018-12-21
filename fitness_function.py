import numpy as np

def fitness_function(solution, transport_cost_matrix, distance_matrix):
    """Funkcja oblicza wartosc funkcji celu dla danego rozwiazania (solution) naszego problemu (QAP) na podstawie macierzy kosztow
    (transport_cost_matrix) i macierzy odleglosci (distance_matrix)."""

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


from read_config import transport_cost_matrix, distance_matrix

if __name__ == '__main__':
    solution = np.array([0,1,2,3,4,5,6,7,8])
    print(fitness_function(solution, transport_cost_matrix, distance_matrix))

