import numpy
import Shapes
import cv2

class Species:


    def __init__(self, Shapes, height, width):
        self.shapes = Shapes;
        self.fitness = 0;
        self.height = height
        self.width = width
        self.image = numpy.zeros((height, width, 3))
        for shape in self.shapes:
            self.image = shape.drawShape(self.image)

    # def drawSpecies(self):
    #     for shape in self.shapes:
    #         self.image = shape.drawShape(self.image)
    #     return self.image

    def __del__(self):
        pass

