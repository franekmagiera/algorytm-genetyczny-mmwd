import random as rnd
import numpy as np
width = 4
length = 4
wtl = width * length

def generate_new_population(lower_bound, upper_bound):

    size = rnd.randrange(lower_bound,upper_bound)
    population = np.zeros((size,wtl),int)
    for i in range(0,size):
        population[i][:] = np.random.permutation(wtl)
    return population