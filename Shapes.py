import cv2

class Shapes:

    def __init__(self, points):
        self.points = points
        self.alpha = 0.00
        # Given in BGR Form
        self.color = [0, 0, 0]

    def drawShape(self, img):
        overlay = numpy.zeros((img.shape[0], img.shape[1], 3))
