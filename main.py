#import Shapes
import Species
# import Genesis

# from naturalSelection import naturalSelection
# from crossover import crossover
from mutation import mutate
from calculateFitness import calculateFitness

# import numpy
# import math
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
    mutationChange = round(amountShapes*0.05)
    height, width, depth = sourceImage.shape

    counter = 0
    evolve = True

    # cv.imshow("Source", sourceImage)
    # cv.waitKey(1)

    parent = Species.Species(amountShapes, height, width,False)
    fitParent = calculateFitness(parent, sourceImage)

    while counter<120:
        child = mutate(parent, mutationChange)
        fitChild = calculateFitness(child, sourceImage)
        if fitChild < fitParent:
            parent = child
            fitParent = fitChild

        #buff = (fitParent / 102586506) * 100
        print("Generation: %i  Fitness: %i" % (counter, fitParent))
        if counter %10 ==0:
            cv.imshow("Parent", parent.image)
            cv.waitKey(1)
        counter += 1

    cv.imshow("Source", parent.image)
    cv.waitKey(0)



