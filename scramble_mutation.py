import random

def scramble_mutation(organism):
    """Funkcja realizuje mutacje scramble."""

    index_from, index_to = random.sample(range(len(organism)), 2)
    if index_from > index_to:
        index_from, index_to = index_to, index_from
    mutation = organism.copy()
    helper = mutation[index_from:index_to]
    random.shuffle(helper)
    mutation[index_from:index_to] = helper
    return mutation

organism = [0,1,2,3,4,5,6,7,8,9]
print(organism)
print(scramble_mutation(organism))

