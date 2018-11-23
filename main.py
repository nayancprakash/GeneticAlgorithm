import Shapes
import Species
import Genesis
# import naturalSelection
# import crossover
# import mutation
import calculateFitness as cF

import numpy
import math
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    # Parameters
    sourceImage = cv.imread(argv[1])
    amountSpecies = 45
    amountShapes = 50
    amountFit =  math.factorial(amountSpecies) / (math.factorial(2)*math.factorial(amountSpecies-2))
    mutationRate = 0.03
    height, width, depth = sourceImage.shape

    # Testing
    gen1 = Genesis.runGenesis(amountSpecies, amountShapes, height, width)
    buff = cF.calculateFitness(gen1,sourceImage)
    # for species in gen1:
    #     species.drawSpecies()
    #     cv.imshow('Species', species.image)
    #     cv.waitKey(0)
    # cv.imshow('Source Image', sourceImage)
    # cv.waitKey(0)



    # population = Genesis.runGenesis(amountSpecies, amountShapes, height, width)
    #
    # evolve = True
    # while evolve:
    #
    #     speciesFitness = cF.calculateFitness(population, sourceImage)
    #     matingPool = naturalSelection(population,speciesFitness)
    #     childPool = crossover(matingPool)
    #     population = mutation(childPool)



