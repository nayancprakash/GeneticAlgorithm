import numpy
import Shapes
import cv2

class Species:

    def __init__(self, Shapes, width, height):
        self.shapes = Shapes;
        self.fitness = 0;
        self.image = numpy.zeros((width, height, 3))

    def drawSpecies(self):
        for shape in self.shapes:
            self.image = shape.drawShape(self.image)
        return self.image


    def getFitness(self, img):
        for x in range(self.image.shape[0]):
            for y in range(self.image.shape[1]):
                deltaB = abs(img[x][y][0] - self.image[x][y][0])
                deltaG = abs(img[x][y][1] - self.image[x][y][1])
                deltaR = abs(img[x][y][2] - self.image[x][y][2])
                fitness = deltaB^2 + deltaG^2 + deltaR^2
                return fitness
