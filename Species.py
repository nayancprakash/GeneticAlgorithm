import numpy
import Shapes
import cv2

class Species:


    def __init__(self, Shapes, height, width):
        self.shapes = Shapes;
        self.fitness = 0;
        self.image = numpy.zeros((height, width, 3))

    def drawSpecies(self):
        for shape in self.shapes:
            self.image = shape.drawShape(self.image)
        return self.image


    def getFitness(self, img):
        fitness = 0
        for y in range(self.image.shape[0]):
            for x in range(self.image.shape[1]):
                deltaB = abs(img[y][x][0] - self.image[y][x][0])/16
                deltaG = abs(img[y][x][1] - self.image[y][x][1])/16
                deltaR = abs(img[y][x][2] - self.image[y][x][2])/16
                fitness += deltaB*deltaB + deltaG*deltaG + deltaR*deltaR
        return fitness
