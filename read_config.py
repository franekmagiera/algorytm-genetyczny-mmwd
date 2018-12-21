# skrypt wczytuje dane dla danego problemu z pliku 'input_data'
from types_definitions import Selection_type
from types_definitions import Crossover_type
from types_definitions import Mutation_type
import numpy as np

def read_matrix(file_path):
    """Wczytuje macierz zadana w pliku csv"""

    with open(file_path, 'r') as f:
        data = f.read().splitlines() 
    return np.array([list(map(int, line.split(';'))) for line in data])
 

def is_rectangular(matrix):
    """Sprawdza czy lista list reprezentuje macierz prostokatna"""

    for row in matrix:
        if len(row) != len(matrix[0]):
            return False
    return True


with open('input_data.txt', 'r') as file:
    data = file.read().splitlines()
data = [line.split(';', 1)[0] for line in data]

transport_cost_matrix = read_matrix(data[0])
if not is_rectangular(transport_cost_matrix):
    raise ValueError('Niezgodnosc wymiarow macierzy kosztow - powinna byc prostokatna.')
rows = len(transport_cost_matrix)
columns = len(transport_cost_matrix[0])
penalty_matrix = read_matrix(data[1])
if not is_rectangular(penalty_matrix):
    raise ValueError('Niezgodnosc wymiarow macierzy kar - powinna byc prostokatna.')
if len(penalty_matrix) != rows or len(penalty_matrix[0]) != columns:
    raise ValueError('Niezgodnosc wymiarow macierzy kosztow i kar.')

starting_population = read_matrix(data[2])

if data[3] == 'proportionate':
    selection_method = Selection_type.PROPORTIONATE
elif data[3] == 'ranking':
    selection_method = Selection_type.RANKING
elif data[3] == 'tournament':
    selection_method = Selection_type.TOURNAMENT
else:
    selection_method = Selection_type.TRUNCATION

if data[4] == 'ox':
    crossover_operator = Crossover_type.OX
elif data[4] == 'pmx':
    crossover_operator = Crossover_type.PMX
else:
    crossover_operator = Crossover_type.OX_PMX

mutation_probability = float(data[5])
percentage_of_change = float(data[6])

if data[7] == 'swap':
    mutation_operator = Mutation_type.SWAP
elif data[7] == 'inversion':
    mutation_operator = Mutation_type.INVERSION
else:
    mutation_operator = Mutation_type.SCRAMBLE

distance_matrix = read_matrix(data[8])

iterations_limit = int(data[9])

number_of_parents = int(data[10])

tournament_size = int(data[11])

truncation_threshold = int(data[12])

if __name__ == '__main__':
    print(rows) 
    print(columns) 
    print(transport_cost_matrix)
    print(penalty_matrix)
    print(starting_population)
    print(selection_method)
    print(crossover_operator)
    print(mutation_probability)
    print(percentage_of_change)
    print(mutation_operator)
    print(distance_matrix)
    print(iterations_limit)
    print(number_of_parents)
    print(tournament_size)
    print(truncation_threshold)


