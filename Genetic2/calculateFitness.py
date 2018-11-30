import numpy

def calculateFitness(population, sourceImage):
    for species in population:
        fitness = 0
        delta = sourceImage - species.image
        fitness = delta * delta
        fitness = numpy.sum(fitness)
        species.fitness = fitness
