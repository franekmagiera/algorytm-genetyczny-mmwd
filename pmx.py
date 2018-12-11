import random
import numpy as np

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
    
#
if __name__ == '__main__':
    parent1 = [1,5,2,8,7,4,3,6]
    parent2 = [4,2,5,8,1,3,6,7]

    parent3 = np.array([8,4,7,3,6,2,5,1,9,0])
    parent4 = np.arange(10)

    child1, child2 = pmx(parent1,parent2)
    print(child1, child2)
    child3, child4 = pmx(parent3, parent4)
    print(child3, child4)
    print(type(child1))

