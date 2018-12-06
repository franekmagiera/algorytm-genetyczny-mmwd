import random
import numpy as np

def generate_new_population(lower_bound, upper_bound, permutation_length):
    """Funkcja generuje macierz ktorej wiersze to permutacje bedace rozwiazaniami naszego problemu.
    Ilosc wierszy jest losowa i zawiera sie w przedziale od lower_bound do upper_bound.
    Korzystamy z prealokacji w celu przyspieszenia obliczen."""

    size = random.randrange(lower_bound, upper_bound)
    population = np.zeros((size, permutation_length), int)
    for i in range(size):
        population[i] = np.random.permutation(permutation_length)
    return population

