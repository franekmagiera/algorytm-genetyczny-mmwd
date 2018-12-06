import random
import numpy as np

def ox_helper_function(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji ox. Powstała, aby uniknąć duplikacji kodu"""

    child = np.full(len(parent1), -1)
    child[index_from:index_to] = parent1[index_from:index_to]
    helper = [x for x in parent2 if x not in parent1[index_from:index_to]]
    i = 0
    for x in np.nditer(child, op_flags=['readwrite']):
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
parent1 = np.array([2,5,8,7,4,1,3,6])
parent2 = np.array([8,7,2,5,1,4,6,3])

child1, child2 = ox(parent1, parent2)

print(child1, child2)

