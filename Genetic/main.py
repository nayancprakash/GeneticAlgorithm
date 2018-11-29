import numpy
import cv2 as cv
from sys import argv

import Shapes
import Species
from calculateFitness import calculateFitness
from crossover import crossover
from Genesis import runGenesis
from mutate import mutate

if __name__ == "__main__":
    sourceImage = cv.imread(argv[1])
    amountSpecies = 30
    amountShapes = 100
    amountVertices = 3
    amountFit = 15
    mutationRate = 0.02
    mutationAmount = 0.05
    height, width, depth = sourceImage.shape

    population = runGenesis(amountSpecies, amountShapes, height, width, amountVertices)
    evolve = True
    counter = 0
    for species in population:
        cv.imshow("Stuff", species.image)
        cv.waitKey(100)
    while evolve:
        calculateFitness(population, sourceImage)
        population = sorted(population, key=lambda x: x.fitness, reverse=False)
        fittest = population[0]
        print("Generation: %i Fitness: %i" % (counter, fittest.fitness))
        print(population[len(population)-1].fitness)
        cv.imshow("Source", population[0].image)
        cv.waitKey(1)
        population = crossover(population[0:amountFit], amountFit)
        population = mutate(population, mutationRate, mutationAmount)
        population.append(fittest)
        counter += 1
