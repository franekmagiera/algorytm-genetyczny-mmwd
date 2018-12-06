# skrypt wczytuje dane dla danego problemu z pliku 'input_data'
from types_definitions import Selection_type
from types_definitions import Crossover_type
from types_definitions import Mutation_type
from types_definitions import Succession_type
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

if data[3] == 'proportional':
    selection_method = Selection_type.PROPORTIONAL
elif data[3] == 'ranking-linear':
    selection_method = Selection_type.RANKING_LINEAR
elif data[3] == 'ranking-non-linear':
    selection_method = Selection_type.RANKING_NON_LINEAR
elif data[3] == 'tournament':
    selection_method = Selection_type.TOURNAMENT
else:
    selection_method = Selection_type.THRESHOLD

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
elif data[7] == 'shift':
    mutation_operator = Mutation_type.SHIFT
else:
    mutation_operator = Mutation_type.SHUFFLE

if data[8] == 'elite':
    succession_method = Succession_type.ELITE
else:
    succession_method = Succession_type.CLEAN

distance_matrix = read_matrix(data[9])

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
print(succession_method)
print(distance_matrix)

