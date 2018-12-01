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
        self.a = random.randint(0, 200)
        self.b = random.randint(0, 255)
        self.g= random.randint(0, 255)
        self.r = random.randint(0, 255)

        self.color = (random.randint(0,256), random.randint(0,256), random.randint(0,256), random.randint(0, 200))

    def drawShape(self, img):
        width, height = img.size
        #overlay = numpy.zeros((height, width, 4))
        canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        painting = ImageDraw.Draw(canvas)
        painting.polygon(self.points, (self.r,self.g,self.b,self.a), (self.r,self.g,self.b,self.a))
        img.paste(canvas, canvas)
        return img
        #overlay1 = Image.fromarray(overlay, "RGBA")
        #canvas = ImageDraw.Draw(overlay1)
        #canvas.polygon(self.points, self.color)
        #return numpy.asarray(overlay1)
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
