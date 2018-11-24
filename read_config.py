# skrypt wczytuje dane dla danego problemu z pliku 'input_data'
def read_matrix(file_path):
    """Wczytuje macierz zadana w pliku csv"""

    with open(file_path, 'r') as f:
        data = f.read().splitlines() 
    return [list(map(int, line.split(';'))) for line in data]
 

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
starting_population_size = int(data[2])
selection_method = data[3]
crossover_operator = data[4]
mutation_probability = float(data[5])
mutation_operator = data[6]
succession_method = data[7]


print(rows) 
print(columns) 
print(transport_cost_matrix)
print(penalty_matrix)
print(starting_population_size)
print(selection_method)
print(crossover_operator)
print(mutation_probability)
print(mutation_operator)
print(succession_method)

