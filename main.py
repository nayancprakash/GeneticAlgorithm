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
    amountShapes = 50
    amountFit = 10
    mutationRate = 5
    mutationChange = round(amountShapes*0.1)
    height, width, depth = sourceImage.shape
    maxErr = (((width*height*255)^2)*3)

    population = Genesis.runGenesis(amountSpecies, amountShapes, height, width)

    counter = 0
    evolve = True

    # cv.imshow("Source", sourceImage)
    # cv.waitKey(0)
    # tracker = SummaryTracker()
    while counter<100:

        speciesFitness = None
        speciesFitness = []
        # start = time.time()
        speciesFitness = calculateFitness(population, sourceImage)
        # end = time.time()
        # print(start-end)

        matingPool =None
        matingPool = []
        fittest = None
        # start = time.time()
        (matingPool,fittest) = naturalSelection(population, speciesFitness, amountFit)
        # end =time.time()
        # print(start-end)
        childPool = None
        childPool =[]
        # start=time.time()
        childPool = crossover(matingPool)
        # end = time.time()
        # print(start-end)
        population = None
        population = []
        # start = time.time()
        population = mutation(childPool,mutationRate, mutationChange)
        # end = time.time()
        # print(start-end)

        print("Generation: %i Fitness: %f" % (counter,((maxErr-fittest.fitness)/maxErr)*100))
        # cv.imshow("Fittest Species", fittest.image)
        # cv.waitKey(1)
        counter+= 1
        # tracker.print_diff()
    cv.imshow("Source", fittest.image)
    cv.waitKey(0)
    # tracker = SummaryTracker()



