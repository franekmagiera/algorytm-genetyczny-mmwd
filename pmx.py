import random

def pmx_helper_function(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji pmx. Powstała, aby uniknąć duplikacji kodu."""

    child = [None for i in range(len(parent1))]
    child[index_from:index_to] = parent2[index_from:index_to]
    mapping = {x: y for x,y in zip(parent2[index_from:index_to],
                                    parent1[index_from:index_to])}
    for index, value in enumerate(parent1):
        if child[index] is not None:
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
parent1 = [1,5,2,8,7,4,3,6]
parent2 = [4,2,5,8,1,3,6,7]

child1, child2 = pmx(parent1,parent2)
print(child1, child2)

