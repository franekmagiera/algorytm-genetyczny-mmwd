from read_config import transport_cost_matrix, distance_matrix, starting_population, iterations_limit, selection_method, crossover_operator, mutation_probability, percentage_of_change, mutation_operator
from fitness_function import fitness_function
from crossover_operators import ox, pmx
from selection_operators import proportionate_selection, truncation_selection
from mutation_operators import inversion_mutation, scramble_mutation, swap_mutation
from types_definitions import Selection_type, Crossover_type, Mutation_type
import random
import numpy as np
import matplotlib.pyplot as plt

fitness_f = lambda solution: fitness_function(solution, transport_cost_matrix, distance_matrix)

if __name__ == '__main__':
    # wybieramy rodzaj selekcji 
    if selection_method == Selection_type.PROPORTIONATE:
        selection_f = proportionate_selection
    elif selection_method == Selection_type.RANKING:
        pass
    elif selection_method == Selection_type.TOURNAMENT:
        pass
    else:
        selection_f = truncation_selection

    # wybieramy rodzaj krzyzowania
    if crossover_operator == Crossover_type.OX:
        crossover_f = ox
    elif crossover_operator == Crossover_type.PMX:
        crossover_f = pmx
    else:
        pass

    # wybieramy rodzaj mutacji
    if mutation_operator == Mutation_type.SWAP:
        mutation_f = swap_mutation
    elif mutation_operator == Mutation_type.INVERSION:
        mutation_f = inversion_mutation
    else:
        mutation_f = scramble_mutation

    population_size = np.size(starting_population, 0)
    permutation_size = np.size(starting_population, 1)
    children = np.zeros((population_size*(population_size-1), permutation_size), int)
    population = np.copy(starting_population)
    best_solutions = np.zeros((iterations_limit, permutation_size), int)
    global_best_solutions = np.zeros((iterations_limit, permutation_size), int) 
    iterations_counter = 0
    
    while iterations_counter < iterations_limit:
        # tworzymy nowych potomkow na podstawie poprzedniej populacji
        children_counter = 0
        for i in range(population_size-1):
            for j in range(i+1, population_size):
                children[children_counter], children[children_counter+1] = crossover_f(population[i], population[j])
                children_counter += 2
        # kazdy potomek ulega mutacji o okreslonym wplywie na gen i z zadanym prawdopodobienstwem
        for child in children:
            if random.random() < mutation_probability:
                child = mutation_f(child, percentage_of_change)
        # dokonujemy selekcji
        population = selection_f(children, population_size, fitness_f)
        # zbieramy dane do statystyk
        fitness_values = [fitness_f(population[i]) for i in range(population_size)]
        best_in_current_iteration = fitness_values.index(min(fitness_values))
        best_solutions[iterations_counter] = population[best_in_current_iteration]
        if iterations_counter == 0:
            global_best_solutions[iterations_counter] = population[best_in_current_iteration]
        elif fitness_f(global_best_solutions[iterations_counter-1]) > fitness_f(population[best_in_current_iteration]):
            global_best_solutions[iterations_counter] = population[best_in_current_iteration]
        else:
            global_best_solutions[iterations_counter] = global_best_solutions[iterations_counter-1]
        iterations_counter += 1

    print(global_best_solutions[iterations_limit-1])
    print(fitness_f(global_best_solutions[iterations_limit-1]))
    best_solutions_values = np.array([fitness_f(best_solutions[i]) for i in range(len(best_solutions))])
    global_best_solutions_values = np.array([fitness_f(global_best_solutions[i]) for i in range(len(global_best_solutions))])
    iterations = np.arange(1, iterations_limit+1)
    plt.plot(iterations, best_solutions_values, 'r', label='W danej iteracji')
    plt.plot(iterations, global_best_solutions_values, 'b', label='Globalnie')
    plt.legend(loc='upper right')
    plt.xlabel('Iteracje')
    plt.ylabel('Wartosc funkcji celu')
    plt.title('Przebieg wartosci najlepszych rozwiazan')
    plt.show()

