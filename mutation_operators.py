import random
import numpy as np


def inversion_mutation(organism, percentage_of_change):
    """Funkcja realizuje mutacje genu poprzez inwersje."""
    index_from = random.randrange(0, int(len(organism)*(1-percentage_of_change)))
    index_to = index_from + int(len(organism)*percentage_of_change)
    return np.concatenate((organism[:index_from], np.flip(organism[index_from:index_to]), organism[index_to:]))


def scramble_mutation(organism, percentage_of_change):
    """Funkcja realizuje mutacje scramble."""

    index_from = random.randrange(0, int(len(organism)*(1-percentage_of_change)))
    index_to = index_from + int(len(organism)*percentage_of_change)
    mutation = np.copy(organism)
    helper = mutation[index_from:index_to]
    np.random.shuffle(helper)
    mutation[index_from:index_to] = helper
    return mutation


def swap_mutation(organism, percentage_of_change):
    """Funkcja realizuje mutacje genu poprzez zamiane"""
    
    x, y = random.sample(range(len(organism)-1), 2)
    mutation = np.copy(organism)
    mutation[x], mutation[y] = mutation[y], mutation[x]
    return mutation
