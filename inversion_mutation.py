import random
import numpy as np

percentage_of_change = 0.3

def inversion_mutation(organism):
    """Funkcja realizuje mutacje genu poprzez inwersje."""
    index_from = random.randrange(0, int(len(organism)*(1-percentage_of_change)))
    index_to = index_from + int(len(organism)*percentage_of_change)
    return np.concatenate((organism[:index_from], np.flip(organism[index_from:index_to]), organism[index_to:]))


organism = np.arange(20)
mutated = inversion_mutation(organism)
print(organism)
print(mutated)
