from PIL import Image
import numpy
from sys import argv

import Shapes
import Species
from calculateFitness import calculateFitness
from crossover import crossover
from Genesis import runGenesis
from mutate2 import mutate

if __name__ == "__main__":
    sourceImage = Image.open(argv[1])
    amountSpecies = 50
    amountShapes = 75
    amountVertices = 3
    amountFit = 7
    mutationRate = 0.07
    mutationAmount = 0.10
    width, height = sourceImage.size
    print(height)
    print(width)
    #print(numpy.asarray(sourceImage))
    #sourceImage.show()
    #print(numpy.asarray(sourceImage))
    population = runGenesis(amountSpecies, amountShapes, height, width, amountVertices)
    evolve = True
    counter = 0
    population[0].image.show()
    #Image.fromarray(population[0].image).show()
    #Image.fromarray(population[0].image).show()
    #for species in population:
        # Image.fromarray(species.image).show()
    while evolve:
        calculateFitness(population, sourceImage)
        population = sorted(population, key=lambda x: x.fitness, reverse=False)
        print(len(population))
        #population = population[0:amountFit]
        fittest = population[0]
        print("Generation: %i Fitness: %i" % (counter, fittest.fitness))
        print(population[len(population)-1].fitness)
        if counter % 8 == 0:
            population[0].image.show()
        #Image.fromarray(population[0].image).show()
        #cv.imshow("Source", population[0].image)
        #cv.waitKey(1)
        population = crossover(population[0:amountFit], amountFit)
        population = mutate(population, mutationRate, mutationAmount)
        #children = []
        #children = crossover(population, amountFit)
        #children = mutate(children, mutationRate, mutationAmount)
        #population.extend(children)
        population.append(fittest)
        counter += 1
