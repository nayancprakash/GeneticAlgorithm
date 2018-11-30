import numpy
import Species

def calculateFitness(population, sourceImage):
    for species in population:
        fitness = 0
        delta = numpy.asarray(sourceImage) - numpy.asarray(species.image)
        fitness = delta * delta
        fitness = numpy.sum(fitness)
        species.fitness = fitness
