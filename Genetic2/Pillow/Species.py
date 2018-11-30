import numpy
import Shapes
from PIL import Image

class Species:


    def __init__(self, Shapes, height, width):
        self.shapes = Shapes;
        self.image = Image.new("RGB", (width, height), (0, 0, 0))
        self.drawSpecies()
        self.fitness = 0;
        self.height = height
        self.width = width

    def drawSpecies(self):
        maskList = []
        for shape in self.shapes:
            #self.image += (shape.drawShape(self.image)/len(self.shapes))
            #print(shape.drawShape(self.image))
            self.image = shape.drawShape(self.image)
            #maskList.append(shape.drawShape(self.image)/len(self.shapes))
            #maskList.append(shape.drawShape(self.image))
        #maskList = numpy.median(maskList, axis=0).astype(numpy.uint8)
        #print(maskList)
        #for mask in maskList:
            #print(mask)
        #self.image = maskList
        # for mask in maskList:
        #     self.image += mask
        # self.image = numpy.round(self.image)
