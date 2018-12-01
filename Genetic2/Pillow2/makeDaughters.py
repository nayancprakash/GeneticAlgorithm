import random
import Species
from PIL import Image, ImageDraw

def makeDaughters(mother, amountChildren, amountVertices):
    population = []
    for i in range(0, amountChildren):
        daughterImage = mother.image.copy()
        width, height = mother.image.size
        alpha = random.randint(0, 2)/10
        xAnchor = round(random.uniform(0, width+1))
        yAnchor = round(random.uniform(0, height+1))
        r = random.randint(2, 30)
        ellipse = (xAnchor, yAnchor, xAnchor + r, yAnchor + r)
        #pointsList = []
        #for i in range(0, amountVertices):
            #pointsList.append((xAnchor + random.triangular(0, width), yAnchor + random.triangular(0, height)))

        #points = pointsList
        a = random.randint(0, 125)
        b = random.randint(0, 256)
        g= random.randint(0, 256)
        r = random.randint(0, 256)

        #newCreature = creature.img
        canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        painting = ImageDraw.Draw(canvas)
        #painting.polygon(points, (r,g,b,a), (r,g,b,a))
        painting.ellipse(ellipse, (r,g,b,a), (r,g,b,a))
        daughterImage.paste(canvas, canvas)
        daughter = Species.Species(daughterImage)
        population.append(daughter)
    return population
