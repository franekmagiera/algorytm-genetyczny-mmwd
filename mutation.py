mutation_probability = 0.30
mutation_operator = "scramble"
print(mutation_operator)

organism = [1,2,3,4,5,6,7,8,9,10]

import random

def mutation(org):

    prob = random.random()
    print(prob)

    if mutation_probability >= prob:

        if mutation_operator == "inversion":
            x = random.randrange(0, len(org))
            y = random.randrange(0, len(org))
            print(x)
            print(y)
            if y<x:
                x,y = y,x
            temp = organism[x:y]
            print(temp)
            temp.reverse()
            organism[x:y] = temp

        elif mutation_operator == "swap":
            x = random.randrange(0,len(org))
            y = random.randrange(0,len(org))
            print(x)
            print(y)
            org[x], org[y] = org[y], org[x]

        elif mutation_operator == "scramble":
            x = random.randrange(0, len(org))
            y = random.randrange(0, len(org))
            print(x)
            print(y)
            if y < x:
                x, y = y, x
            temp = organism[x:y]
            print(temp)
            random.shuffle(temp)
            organism[x:y] = temp

    return org

print(mutation(organism))

