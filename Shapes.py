import cv2 as cv
import random
import numpy

class Shapes:

    alpha = 0.00
    points = []
    color = []

    def __init__(self, height, width):
        polyOverflow = 75
        self.alpha = random.randrange(0, 5)/10000
        pointsList = []
        for i in range(0, random.randint(3,6)):
            pointsList.append([random.randint(-polyOverflow,width+polyOverflow), random.randint(-polyOverflow,height+polyOverflow)])
        self.points = pointsList
        # Given in BGR Form
        self.color = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]

    def drawShape(self, img):
        height, width, depth = img.shape
        overlay = numpy.zeros((height, width, 3))
        #print('\n' + self.color)
        cv.fillPoly(overlay, [numpy.array(self.points)], (self.color[0], self.color[1], self.color[2]))
        #cv.addWeighted(overlay, self.alpha, img, 1-self.alpha, 0.0, img)
        img = img*(1-self.alpha)+overlay*self.alpha
        return img
