import random
import Shapes
import Species

def mutation(pop,rate, numChange):

    for i in range(len(pop)):
        randInt = random.randint(0,100)
        if randInt <= rate:
            randMutate = random.randint(0,100)
            if randMutate <= 15:
                mutate1(pop[i])
            elif randMutate <= 50:
                mutate2(pop[i])
            elif randMutate <= 101:
                pop[i] = mutate3(pop[i], numChange)
    return pop


def mutate1(species):
    height = species.height
    width = species.width
    randInt = random.randint(0, len(species.shapes)-1)
    species.shapes[randInt].smallMutate(height, width)

def mutate2(species):
    height = species.height
    width = species.width
    for i in range(0, 5):
        randInt = random.randint(0, len(species.shapes)-1)
        species.shapes[randInt].smallMutate(height, width)

def mutate3(species, numChange):
    height = species.height
    width = species.width
    shapes = []

    for i in range(len(species.shapes)):
        if i < numChange:
            shapes.append(Shapes.Shapes(height, width, 10))
        else:
            shapes.append(species.shapes[i])
    newSpecies = Species.Species(shapes, height, width)

    return newSpecies
