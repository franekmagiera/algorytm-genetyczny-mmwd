import numpy as np

def proportionate_selection(population, number_of_parents, tournament_size, truncation_threshold, fitness_function):
    '''Funkcja realizujaca metode selekcji procentowej (kolo ruletki).'''

    population_size = np.size(population, 0)
    fitness_values = [fitness_function(population[i]) for i in range(population_size)]
    max_fitness = np.amax(fitness_values)
    pom = [2*(max_fitness - x) for x in fitness_values]
    fitness_values = np.add(fitness_values, np.array(pom)) 
    fitness_sum = np.sum(fitness_values)
    probabilities = np.divide(fitness_values, fitness_sum)
    parents_indexes = np.random.choice(np.arange(population_size), size=population_size, replace=False, p=probabilities)
    wybrani = np.array([population[i] for i in range(population_size) if i in parents_indexes]).astype(int)
    wybrani = sorted(wybrani, key=fitness_function)
    return wybrani[:number_of_parents]


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
        parents[i] = (min(tournaments[i][:], key=fitness_function))
    return parents.astype(int)


def truncation_selection(population, number_of_parents, tournament_size, truncation_threshold, fitness_function):

    population_size = np.size(population, 0)
    population_copy = np.copy(population)
    population_copy = sorted(population_copy, key=fitness_function)
    truncation = int((truncation_threshold/100) * population_size)
    parents = np.zeros((truncation, np.size(population, 1)))
    for i in range(truncation):
        parents[i] = population_copy[i]
    return parents.astype(int)

