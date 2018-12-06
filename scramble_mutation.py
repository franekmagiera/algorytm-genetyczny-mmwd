import random
import numpy as np

percentage_of_change = 0.3

def scramble_mutation(organism):
    """Funkcja realizuje mutacje scramble."""

    index_from = random.randrange(0, int(len(organism)*(1-percentage_of_change)))
    index_to = index_from + int(len(organism)*percentage_of_change)
    mutation = np.copy(organism)
    helper = mutation[index_from:index_to]
    np.random.shuffle(helper)
    mutation[index_from:index_to] = helper
    return mutation


organism = np.arange(20)
print(organism)
print(scramble_mutation(organism))
