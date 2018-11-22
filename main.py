import Shapes
import Species
import Genesis
import numpy
import math
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    sourceImage = cv.imread(argv[1])
    amountFittest = 50
    amountShapes = 50
    amountCombinations =  math.factorial(amountFittest) / (math.factorial(2)*math.factorial(amountFittest-2))
    mutationRate = 0.03
    height, width, depth = sourceImage.shape
    gen1 = Genesis.runGenesis(amountFittest, amountShapes, height, width)
    for species in gen1:
        #print(species.getFitness(sourceImage))
        species.drawSpecies()
        cv.imshow('Species', species.image)
        cv.waitKey(0)
    cv.imshow('Source Image', sourceImage)
    cv.waitKey(0)
