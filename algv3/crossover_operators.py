import random
import numpy as np

def ox_helper_function(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji ox. 
    Wzorowany na wersji zaproponowanej przez Davisa."""

    child = np.full(len(parent1), -1)
    child[index_from:index_to] = parent1[index_from:index_to]
    helper = [x for x in parent2 if x not in parent1[index_from:index_to]]
    i = 0
    with np.nditer(child, op_flags=['readwrite']) as it:
        for x in it:
            if x == -1:
                x[...] = helper[i]
                i += 1
    return child


def ox_helper_function2(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji ox.
    Wersja druga, wzorowana na wersji zaproponowanej przez Goldberga."""

    child = np.full(len(parent1), -1)
    child[index_from:index_to] = parent1[index_from:index_to]
    helper = [x for x in np.concatenate((parent2[index_from:], parent2[:index_from])) if x not in parent1[index_from:index_to]]
    i = 0
    with np.nditer(child, op_flags=['readwrite']) as it:
        for x in it:
            if x == -1:
                x[...] = helper[i]
                i += 1  
    return child


def ox(parent1, parent2):
    """Funkcja realizująca operator Order crossover.
    
    Jako argumenty pobiera dwóch rodziców.
    Funkcja zwraca krotkę zawierającą dwóch potomków.
    """

    if len(parent1) != len(parent2):
        raise ValueError("Argumenty powinny być tej samej długości.")
    index_from, index_to = random.sample(range(0, len(parent1)), 2)
    if index_from > index_to:
        index_from, index_to = index_to, index_from
    # zapewnienie nie kopiowania całego rodzica
    if index_to - index_from == len(parent1):
        index_to -= 2
    return (ox_helper_function(parent1, parent2, index_from, index_to),
    ox_helper_function(parent2, parent1, index_from, index_to))

	
def pmx_helper_function(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji pmx. Powstała, aby uniknąć duplikacji kodu."""

    child = np.full(len(parent1), -1)
    child[index_from:index_to] = parent1[index_from:index_to]
    mapping = {x: y for x,y in zip(parent1[index_from:index_to], parent2[index_from:index_to])}
    for index, value in enumerate(parent2):
        if child[index] != -1:
            continue
        elif value not in child:
            child[index] = value
        else:
            v = value
            while v in mapping:
                v = mapping[v]
            child[index] = v
    return child


def pmx(parent1, parent2):
    """Funkcja realizująca operator Partially-mapped crossover.

    Jako argumenty pobiera dwóch rodziców.
    Funkcja zwraca krotkę zawierającą dwóch potomków.
    """

    if len(parent1) != len(parent2):
        raise ValueError("Argumenty powinny być tej samej długości.")
    index_from, index_to = random.sample(range(0, len(parent1)), 2)
    if index_from > index_to:
        index_from, index_to = index_to, index_from
    # zapewnienie nie kopiowania calego rodzica
    if index_to - index_from == len(parent1):
        index_to -= 2
    return (pmx_helper_function(parent1, parent2, index_from, index_to),
    pmx_helper_function(parent2, parent1, index_from, index_to))

