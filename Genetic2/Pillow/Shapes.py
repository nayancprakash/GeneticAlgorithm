import random
import numpy
from PIL import Image, ImageDraw

class Shapes:

    def __init__(self, height, width, amountVertices):
        self.alpha = random.randint(0, 2)/10
        xAnchor = round(random.uniform(0, width+1))
        yAnchor = round(random.uniform(0, height+1))
        pointsList = []
        for i in range(0, amountVertices):
            pointsList.append((xAnchor + random.randint(round(-1*width/2), round(width/2)), yAnchor + random.randint(round(-1*height/2), round(height/2))))

        self.points = pointsList
        self.color = (random.randint(0,256), random.randint(0,256), random.randint(0,256))

    def drawShape(self, img):
        height, width, depth = img.shape
        overlay = numpy.zeros((height, width, 3))
        overlay1 = Image.fromarray(overlay, "RGB")
        canvas = ImageDraw.Draw(overlay1)
        canvas.polygon(self.points, self.color, self.color)
        return numpy.asarray(overlay1)
        #print(canvas)
        #print(numpy.asarray(Image.blend(Image.fromarray(img, "RGB"), overlay1, 0.5)))
        #return numpy.asarray(Image.blend(Image.fromarray(img, "RGB"), overlay1, 0.5))

        #print('\n' + self.color)
        #cv3.fillPoly(overlay, [numpy.array(self.points)], (self.color[0], self.color[1], self.color[2]))
        #cv.addWeighted(overlay, self.alpha, img, 1-self.alpha, 0.0, img)
        #return (overlay*self.alpha)
        #img = img*(1-self.alpha) + delta*self.alpha
        #img = img*(1-self.alpha)+overlay*self.alpha
        #img = img+overlay*self.alpha
        #return img
