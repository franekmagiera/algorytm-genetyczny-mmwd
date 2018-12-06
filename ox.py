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

#
parent1 = np.array([9,8,4,5,6,7,1,3,2,0])
parent2 = np.array([8,7,1,2,3,0,9,5,4,6])

parent3 = np.array([1,2,3,4,5,6,7,8,9])
parent4 = np.array([5,7,4,9,1,3,6,2,8])

child1, child2 = ox(parent1, parent2)
child4, child3 = ox(parent3, parent4)

print(child1, child2, child3, child4)

