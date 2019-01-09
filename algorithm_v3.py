from read_config import starting_population, iterations_limit
from read_config import mutation_probability, percentage_of_change
from read_config import number_of_parents, tournament_size, truncation_threshold
from read_config import crossover_operator, mutation_operator, selection_method, succession_method

from fitness_function import fit_fun

from selection_operators import tournament_selection, truncation_selection, proportionate_selection
from crossover_operators import pmx, ox
from mutation_operators import inversion_mutation, scramble_mutation, swap_mutation
from succession_operators import children_only, mixed

from types_definitions import SelectionType, CrossoverType, MutationType, SuccessionType

import random
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    if selection_method == SelectionType.PROPORTIONATE:
        selection_f = proportionate_selection
    elif selection_method == SelectionType.TOURNAMENT:
        selection_f = tournament_selection
    else:
        selection_f = truncation_selection

    if crossover_operator == CrossoverType.OX:
        crossover_f = ox
    elif crossover_operator == CrossoverType.PMX:
        crossover_f = pmx
    else:
        pass

    if mutation_operator == MutationType.SWAP:
        mutation_f = swap_mutation
    elif mutation_operator == MutationType.INVERSION:
        mutation_f = inversion_mutation
    else:
        mutation_f = scramble_mutation

    if succession_method == SuccessionType.MIXED:
        succession_f = mixed
    else:
        succession_f = children_only

    population_size = np.size(starting_population, 0)
    permutation_size = np.size(starting_population, 1)
    population = np.copy(starting_population)
    best_solutions = np.zeros((iterations_limit, permutation_size))
    worst_solutions = np.zeros((iterations_limit, permutation_size))
    best_values = np.zeros((iterations_limit+1, 1))
    worst_values = np.zeros((iterations_limit+1, 1))
    global_best_values = np.zeros((iterations_limit+1, 1))
    global_best_solutions = np.zeros((iterations_limit, permutation_size))
    global_best_value = 0
    iteration_counter = 0
    tolerance = 0

    while iteration_counter < iterations_limit:
        children = []
        parents = selection_f(population, number_of_parents, tournament_size, truncation_threshold, fit_fun)
        for i in range(int(number_of_parents)):
            x, y = random.sample(range(len(parents)), 2)
            child1, child2 = crossover_f(parents[x], parents[y])
            children.append(child1)
            children.append(child2)
        for i in range(len(children)):
            if random.random() < mutation_probability:
                children[i] = mutation_f(children[i], percentage_of_change)
        population = succession_f(population_size, children, parents)
        best_solutions[iteration_counter] = min(population, key=fit_fun)
        worst_solutions[iteration_counter] = max(population, key=fit_fun)
        best_values[iteration_counter] = int(fit_fun(best_solutions[iteration_counter].astype(int)))
        worst_values[iteration_counter] = int(fit_fun(worst_solutions[iteration_counter].astype(int)))
        population_size = np.size(population, 0)
        if best_values[iteration_counter] >= global_best_value:
            tolerance += 1
        else:
            tolerance = 0
        if tolerance == 250:
            print('Breaking after', iteration_counter, 'iterations')
            break
        iteration_counter += 1
        global_best_value = int(min(best_values[:iteration_counter]))

    minimum = best_values[0]
    global_best_values[0] = best_values[0]
    for i in range(1, iteration_counter):
        if best_values[i] < minimum:
            minimum = best_values[i]
        global_best_values[i] = minimum
    global_best_solution = min(best_solutions[:iteration_counter].astype(int), key=fit_fun)
    print('Best solution: ', global_best_solution, 'with value of: ', global_best_value)
    x_axis_limit = np.arange(iteration_counter)
    plt.plot(x_axis_limit, best_values[:iteration_counter], 'g', label='Najlepsze rozwiązania')
    plt.plot(x_axis_limit, worst_values[:iteration_counter],'r', label='Najgorsze rozwiązania')
    plt.plot(x_axis_limit, global_best_values[:iteration_counter], 'b--', label='Globalnie najlepsze rozwiązanie')
    plt.yticks(np.arange(global_best_value, max(worst_values), step=700))
    plt.xticks(np.arange(iteration_counter, step=int(iteration_counter/15)+1))
    plt.xlabel('Numer iteracji')
    plt.ylabel('Wartość funkcji celu')
    plt.title('Przebieg działania algorytmu')
    plt.legend()
    plt.show()

