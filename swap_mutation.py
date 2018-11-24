import random

def swap_mutation(organism):
    """Funkcja realizuje mutacje genu poprzez zamiane"""
    
    x, y = random.sample(range(len(organism)-1), 2)
    mutation = organism.copy()
    mutation[x], mutation[y] = mutation[y], mutation[x]
    return mutation


organism = [1,2,3,4,5,6,7,8,9]
print(organism)
print(swap_mutation(organism))

