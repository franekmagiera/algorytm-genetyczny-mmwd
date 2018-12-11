from read_config import transport_cost_matrix, distance_matrix, starting_population
from fitness_function import fitness_function
from pmx import pmx
import numpy as np
import matplotlib.pyplot as plt

fitness_function2 = lambda solution: fitness_function(solution, transport_cost_matrix, distance_matrix)

if __name__ == '__main__':
    iterations_limit = 20
    counter = 0
    population_size = np.size(starting_population, 0)
    permutation_size = np.size(starting_population, 1)
    children = np.zeros((population_size*(population_size-1), permutation_size), int)
    population = np.copy(starting_population)
    best_solutions = np.zeros((iterations_limit, permutation_size), int)
    best_solution = 0
    while counter < iterations_limit:
        counter += 1
        counter2 = 0
        for i in range(population_size-1):
            for j in range(i+1, population_size):
                children[counter2], children[counter2+1] = pmx(population[i], population[j])
                counter2 += 2
        population_values = [fitness_function2(population[x]) for x in range(len(population))]
        children_values = [fitness_function2(children[x]) for x in range(len(children))]
        population_order = np.argsort(population_values)
        children_order = np.argsort(children_values)
        population = population[population_order]
        children = children[children_order]
        best_solutions[counter-1] = population[0] if fitness_function2(population[0]) < fitness_function2(children[0]) else children[0] 
        if counter == 1:
            best_solution = best_solutions[0]
        elif fitness_function2(best_solutions[counter-1]) < fitness_function2(best_solution):
            best_solution = best_solutions[counter-1]
        population[:] = children[:population_size]
    print(best_solution)
    print(fitness_function2(best_solution))
    best_solutions_values = np.array([fitness_function2(best_solutions[x]) for x in range(len(best_solutions))])
    iterations = np.arange(1,iterations_limit+1)
    plt.plot(iterations, best_solutions_values)
    plt.xlabel('Iteracje')
    plt.ylabel('Wartosc funkcji celu najlepszego dotychczasowego rozwiazania')
    plt.title('Przebieg wartosci najlepszego rozwiazania')
    plt.show()

