import numpy as np


def proportionate_selection(population, number_of_parents, tournament_size, truncation_threshold, fitness_function):
    parents = np.zeros((number_of_parents, np.size(population, 1)))  # preallocation of parents vector
    population_size = np.size(population, 0)
    fitness_values = [fitness_function(population[i]) for i in range(population_size)]
    max_fitness = np.amax(fitness_values)  # highest (worst) fitness function value
    fitness_values = np.subtract(fitness_values, max_fitness)
    # solutions with lower fitness function values need to have a larger probability of becoming a parent
    fitness_sum = np.sum(fitness_values)
    probabilities = np.divide(fitness_values, fitness_sum)
    parents_indexes = np.random.choice(np.arange(population_size), size=number_of_parents, replace=False, p=probabilities)
    return np.array([population[i] for i in range(population_size) if i in parents_indexes]).astype(int)


def tournament_selection(population, number_of_parents, tournament_size, truncation_threshold, fitness_function):
    population_size = np.size(population, 0)
    population_copy = np.copy(population)
    number_of_parents = int(population_size/tournament_size)
    parents = np.zeros((number_of_parents, np.size(population, 1)))
    tournaments = np.array_split(population_copy, number_of_parents)
    temp_fitness = np.zeros(tournament_size)
    for i in range(number_of_parents):
        for j in range(0, tournament_size):
            temp_fitness[j] = fitness_function(tournaments[i][j])
        #print(temp_fitness)
        #print(tournaments[i][:])
        parents[i] = (min(tournaments[i][:], key=fitness_function))
    return parents.astype(int)


def truncation_selection(population, number_of_parents, tournament_size, truncation_threshold, fitness_function):

    population_size = np.size(population, 0)
    population_copy = np.copy(population)
    population_copy = sorted(population_copy, key=fitness_function)
    truncation = int((truncation_threshold/100) * population_size)
    parents = np.zeros((truncation, np.size(population, 1)))
    #parents = [population_copy[i] for i in range(truncation)]
    for i in range(truncation):
        parents[i] = population_copy[i]
    return parents.astype(int)
