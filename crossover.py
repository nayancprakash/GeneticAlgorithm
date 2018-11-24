import Species
import random


def crossover(pop):
    mating = []

    for i in range(len(pop)):
        for j in range(i,len(pop)):
            if i != j:
                child = cross(pop[i],pop[j])
                mating.append(child)
    return mating

def cross(parent1, parent2):
    height = parent1.height
    width = parent1.width
    shapes = []

    for i in range(len(parent2.shapes)):
        randInt = random.randint(0,100)
        if randInt % 2 == 0:
            shapes.append(parent1.shapes[i])
        else:
            shapes.append(parent2.shapes[i])

    child = Species.Species(shapes,height,width)
    # parent1.image = None
    # parent1.shapes = None
    parent1 = None
    # parent2.image = None
    # parent2.shapes = None
    parent2 = None

    return child




