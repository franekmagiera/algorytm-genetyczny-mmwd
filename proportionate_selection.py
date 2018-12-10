import random as rnd
import numpy as np
import fitness_function as fit
import generate_new_population as gen
from read_config import transport_cost_matrix, distance_matrix


def selection(population, parent_number):
    # realizes a Fitness proportionate selection, A.K.A. roulette wheel selection

    pop = np.copy(population)  # copy of original population
    parents = np.zeros((parent_number, np.shape(pop)[1]))  # allocation of parents vector
    population_count = (np.shape(pop))[0]  # number of population
    each_fitness = np.zeros(population_count)  # fit. fun. value of each individual
    for i in range(0, population_count):  # calculating fit. fun. value for each individual
        each_fitness[i] = fit.fitness_function(pop[i, :], transport_cost_matrix, distance_matrix)
    print('Wart. funkcji celu:', each_fitness)
    max_fitness = np.amax(each_fitness)  # highest (worst) fit. fun. value
    each_fitness = np.subtract(each_fitness, max_fitness)
    # this is a minimization problem, the solutions with low fit. fun. values ought to have a big probability
    print('Wart. po redukcji:', each_fitness)
    fitness_sum = np.sum(each_fitness)  # fitness value of whole population
    probability = np.divide(each_fitness, fitness_sum)  # calculating probability for each individual
    print('Prawdop.:', probability)
    print('suma prawdop.:', np.sum(probability))
    pool = np.arange(population_count)  # vector of indexes to draw lots from
    for i in range(0, parent_number):
        index = rnd.choices(pool, probability)  # choosing a random index with respect to probability
        parents[i] = pop[index, :]  # selecting an individual with chosen index from population to be a parent
        pool = np.delete(pool, index)  # deleting already chosen index from drawing pool
        probability = np.delete(probability, index)  # and from probability vector as well
    return parents.astype(int)


population = gen.generate_new_population(5, 4)
print('Populacja:\n', population, '\n------------')
print('Rodzice:\n', selection(population, 2))

