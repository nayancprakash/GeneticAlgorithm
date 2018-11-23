import numpy
import Shapes
import cv2

class Species:


    def __init__(self, amountShapes, height, width,alphaToggle):
        self.shapes = [];
        self.fitness = 0;
        self.height = height
        self.width = width
        self.image = numpy.zeros((height, width, 3))
        for i in range(amountShapes):
            self.shapes.append(Shapes.Shapes(height, width,alphaToggle))

    def drawSpecies(self):
        for shape in self.shapes:
            self.image = shape.drawShape(self.image)
        return self.image

class Species2:


    def __init__(self, Shapes, height, width):
        self.shapes = Shapes;
        self.fitness = 0;
        self.height = height
        self.width = width
        self.image = numpy.zeros((height, width, 3))

    def drawSpecies(self):
        for shape in self.shapes:
            self.image = shape.drawShape(self.image)
        return self.image

