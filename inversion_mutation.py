import random

def inversion_mutation(organism):
    """Funkcja realizuje mutacje genu poprzez inwersje."""
    index_from, index_to = random.sample(range(len(organism)), 2)
    if index_from > index_to:
        index_from, index_to = index_to, index_from 
    return organism[:index_from] + list(reversed(organism[index_from:index_to])) + organism[index_to:]

organism = [1,2,3,4,5,6,7,8,9]
mutated = inversion_mutation(organism)
print(organism)
print(mutated)
