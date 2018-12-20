import random
import numpy as np
from fitness_function import fitness_function
from generate_new_population import generate_new_population 
from read_config import transport_cost_matrix, distance_matrix


def proportionate_selection(population, number_of_parents):
    '''Funkcja realizujaca metode selekcji procentowej (kolo ruletki).'''

    parents = np.zeros((number_of_parents, np.size(population, 1)))  # preallocation of parents vector
    population_size = np.size(population, 0)
    fitness_values = [fitness_function(population[i], transport_cost_matrix, distance_matrix) for i in range(population_size)]
    # print('Wartosc funkcji celu:', fitness_values)
    max_fitness = np.amax(fitness_values)  # highest (worst) fitness function value
    fitness_values = np.subtract(fitness_values, max_fitness)
    # This is a minimization problem, so solutions with low fitness function values have a larger probabilty of becoming a parent 
    # print('Wartosci po redukcji:', fitness_values)
    fitness_sum = np.sum(fitness_values)  # sum of whole population's fitness values
    probabilities = np.divide(fitness_values, fitness_sum)  # calculating probability of becoming a parent for each individual
    # print('Prawdopodobienstwo:', probabilities)
    # print('Suma prawdopobienstw:', np.sum(probabilities))
    parents_indexes = np.random.choice(np.arange(population_size), size=number_of_parents, replace=False, p=probabilities)
    return np.array([population[i] for i in range(population_size) if i in parents_indexes]).astype(int)

if __name__ == '__main__':
    population = generate_new_population(5, 4)
    print('Populacja:\n', population, '\n------------')
    print('Rodzice:\n', proportionate_selection(population, 2))

