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
        self.shapebuff =[]
        for shape in self.shapes:
            # self.shapebuff.append(shape.drawShape(self.image, len(self.shapes)))
            self.image = shape.drawShape(self.image, len(self.shapes))
        # for i in self.shapebuff:
        #     self.image += i


    # def drawSpecies(self):
    #     for shape in self.shapes:
    #         self.image = shape.drawShape(self.image)
    #     return self.image

    def __del__(self):
        pass

