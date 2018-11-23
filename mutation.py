import random
import Shapes
import Species

def mutation(pop,rate, numChange):

    for i in range(len(pop)):
        randInt = random.randint(0,100)
        if randInt <= rate:
            pop[i] = mutate(pop[i],numChange)
    return pop


def mutate(species,numChange):
    height = species.height
    width = species.width
    shapes = []

    for i in range(len(species.shapes)):
        if i <numChange:
            shapes.append(Shapes.Shapes(height, width,False))
        else:
            shapes.append(species.shapes[i])
    newSpecies = Species.Species2(shapes, height, width)

    return newSpecies



