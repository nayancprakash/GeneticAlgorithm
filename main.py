import Shapes
import Species
import numpy
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    print(argv[1])
    sourceImage = cv.imread(argv[1])
    cv.imshow('Source Image', sourceImage)
    cv.waitKey(0)
