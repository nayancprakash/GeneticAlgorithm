import Shapes
import Species
import Genesis

from naturalSelection import naturalSelection
from crossover import crossover
from mutation import mutation
from calculateFitness import calculateFitness

import numpy
import math
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    # Parameters
    sourceImage = cv.imread(argv[1])
    amountSpecies = 10
    amountShapes = 75
    #amountFit =  math.factorial(amountSpecies) / (math.factorial(2)*math.factorial(amountSpecies-2))
    amountFit = 5
    mutationRate = 3
    mutationChange = round(amountShapes*0.1)
    height, width, depth = sourceImage.shape

    population = Genesis.runGenesis(amountSpecies, amountShapes, height, width)

    counter = 0
    evolve = True

    cv.imshow("Source", sourceImage)
    cv.waitKey(0)

    while evolve:
        speciesFitness = calculateFitness(population, sourceImage)
        (matingPool,fittest) = naturalSelection(population,speciesFitness,amountFit)
        childPool = crossover(matingPool)
        population = mutation(childPool,mutationRate, mutationChange)

        print("Generation: %i Fitness: %i" % (counter,fittest.fitness))
        cv.imshow("Fittest Species", fittest.image)
        cv.waitKey(1)
        counter+= 1
