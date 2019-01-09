import random
import numpy as np

def generate_new_population(population_size, permutation_length):
    """Funkcja generuje macierz ktorej wiersze to permutacje bedace rozwiazaniami naszego problemu.
    Ilosc wierszy zalezy od parametru population_size.
    Korzystamy z prealokacji w celu przyspieszenia obliczen."""

    population = np.zeros((population_size, permutation_length), int)
    for row in range(population_size):
        population[row] = np.random.permutation(permutation_length)
    return population


def save_population_to_file(population, filename):
    """Funkcja zapisuje populacje population do pliku o nazwie filename."""

    np.savetxt(filename, population, delimiter=';', fmt='%d')
    return

if __name__ == '__main__':
    population = generate_new_population(25,36)
    #print(population)
    save_population_to_file(population, 'first_population.csv')

