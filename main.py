import Shapes
import Species
import numpy
import cv2 as cv
from sys import argv

if __name__ == "__main__":
    sourceImage = cv.imread(argv[1])
    cv.imdisplay(sourceImage)
