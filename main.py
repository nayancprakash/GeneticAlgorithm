# import Shapes
# import Species
import Genesis

from naturalSelection import naturalSelection
from crossover import crossover
from mutation import mutation
from calculateFitness import calculateFitness

# import numpy
# import math
# from pympler.tracker import SummaryTracker
# import time
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    # Parameters
    sourceImage = cv.imread(argv[1])
    amountSpecies = 45
    amountShapes = 135
    randAlpha = 5 # in percentage
    amountFit = 5
    mutationRate = 1 # in percentage
    numVertices = 3
    mutationAmount = 10 # in percentage
    height, width, depth = sourceImage.shape
    maxErr = (((width*height*255)^2)*3)

    population = Genesis.runGenesis(amountSpecies, amountShapes, height, width, randAlpha, numVertices)

    counter = 0
    evolve = True

    # cv.imshow("Source", sourceImage)
    # cv.waitKey(0)
    # tracker = SummaryTracker()
    while evolve:

        speciesFitness = None
        speciesFitness = []
        # start = time.time()
        speciesFitness, fittest = calculateFitness(population, sourceImage)
        # end = time.time()
        # print(start-end)
        population = sorted(population, key=lambda x: x.fitness, reverse=False)

        print("Generation: %i Fitness: %f" % (counter,fittest.fitness))
        cv.imshow("Fittest Species", population[0].image)
        cv.waitKey(1)
        # for species in population:
        #     print(species.fitness)
        #matingPool = None
        #matingPool = []
        #fittest = None
        # start = time.time()
        #(matingPool,fittest) = naturalSelection(population, speciesFitness, amountFit)
        print(len(population))
        population = naturalSelection(population, speciesFitness, amountFit)
        print(len(population))
        # end =time.time()
        # print(start-end)
        #childPool = None
        #childPool =[]
        # start=time.time()
        #childPool = crossover(matingPool)
        # end = time.time()
        # print(start-end)
        #population = None
        #population = []
        # start = time.time()
        population = mutation(population, mutationRate, mutationAmount)
        # end = time.time()
        # print(start-end)

        counter+= 1
        # tracker.print_diff()
    cv.imshow("Source", fittest.image)
    cv.waitKey(0)
    # tracker = SummaryTracker()
