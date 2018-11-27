import cv2 as cv
import random
import numpy

class Shapes:

    alpha = 0.00
    points = []
    color = []

    def __init__(self, height, width, randAlpha, numVertices):
        #self.alpha = random.random() * random.random()
        self.alpha = 0.02
        pointsList = []
        xAnchor = random.randint(0,width+1)
        yAnchor = random.randint(0,height+1)
        for i in range(0, numVertices):
            if i == 0:
                pointsList.append([xAnchor, yAnchor])
            else:
                pointsList.append([xAnchor+random.randint(int(-width/5),int(width/5)), yAnchor+random.randint(int(-height/5),int(height/5))])
        self.points = pointsList
        # Given in BGR Form
        self.color = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]

    def drawShape(self, img):
        height, width, depth = img.shape
        overlay = numpy.zeros((height, width, 3))
        cv.fillPoly(overlay, [numpy.array(self.points)], (self.color[0], self.color[1], self.color[2]))
        img = img*(1-self.alpha)+overlay*self.alpha
        return img

    def smallMutate(self, height, width):
        randInt = random.randint(0,100)

        #Add or subtract vertice
        if (randInt % 2 == 0):
            self.points.append([random.randint(0,width+1), random.randint(0,height+1)])
        else:
            if len(self.points) != 3:
                del (self.points[-1])
        #Add or subtract to alpha
        self.alpha += random.randint(-10,10)
        if self.alpha < 0:
            self.alpha = 0
        elif self.  alpha > 1:
            self.alpha = 1
        #Add or subtract to colour
        self.color[0] += random.randint(-20, 20)
        self.color[1] += random.randint(-20, 20)
        self.color[2] += random.randint(-20, 20)
        for i in range(0, 3):
            if self.color[i] < 0:
                self.color[i] = 0
            if self.color[i] > 255:
                self.color[i] = 255
