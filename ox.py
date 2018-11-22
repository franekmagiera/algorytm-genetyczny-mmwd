import random

def ox_helper_function(parent1, parent2, index_from, index_to):
    """Funkcja pomocnicza do funkcji ox. Powstała, aby uniknąć duplikacji kodu"""

    child = [None for i in range(len(parent1))] 
    child[index_from:index_to] = parent1[index_from:index_to]
    copy_parent2 = parent2.copy()
    for index, value in enumerate(copy_parent2):
        if value in child[index_from:index_to]:
           copy_parent2[index] = None
    helper = copy_parent2[index_from-len(copy_parent2):]
    helper.extend(copy_parent2[:index_from])
    helper = [x for x in helper if x is not None]
    i = 0
    for index, value in enumerate(child):
        if value is None:
           child[index] = helper[i]
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
parent1 = [3,5,1,4,7,6,2,8]
parent2 = [4,6,5,1,8,3,2,7]

child1, child2 = ox(parent1, parent2)

print(child1, child2)

