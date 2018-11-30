import numpy
import Shapes
import cv2

class Species:


    def __init__(self, Shapes, height, width):
        self.shapes = Shapes;
        self.image = numpy.zeros((height, width, 3))
        self.drawSpecies()
        self.fitness = 0;
        self.height = height
        self.width = width

    def drawSpecies(self):
        for shape in self.shapes:
            #self.image += (shape.drawShape(self.image)/len(self.shapes))
            self.image += (shape.drawShape(self.image))/len(self.shapes)
