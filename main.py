import Shapes
import Species
import Genesis
import numpy
import math
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    amountFittest = 50
    amountShapes = 50
    amountCombinations =  math.factorial(amountFittest) / (math.factorial(2)*math.factorial(amountFittest-2))
    runGenesis(amountCombinations, amountShapes)
    print(argv[1])
    sourceImage = cv.imread(argv[1])
    cv.imshow('Source Image', sourceImage)
    cv.waitKey(0)
