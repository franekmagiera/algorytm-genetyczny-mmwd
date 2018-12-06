import random
import numpy as np

def swap_mutation(organism):
    """Funkcja realizuje mutacje genu poprzez zamiane"""
    
    x, y = random.sample(range(len(organism)-1), 2)
    mutation = np.copy(organism)
    mutation[x], mutation[y] = mutation[y], mutation[x]
    return mutation


organism = np.arange(20)
print(organism)
print(swap_mutation(organism))

