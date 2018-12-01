from PIL import Image, ImageDraw
import whatup
import random

def addShape(creature,width,height,amountVertices):
        returnPop = []
        for i in range(0,50):
            alpha = random.randint(0, 2)/10
            xAnchor = round(random.uniform(0, width+1))
            yAnchor = round(random.uniform(0, height+1))
            pointsList = []
            for i in range(0, amountVertices):
                pointsList.append((xAnchor + random.randint(round(-1*width/2), round(width/2)), yAnchor + random.randint(round(-1*height/2), round(height/2))))

            points = pointsList
            a = random.randint(0, 200)
            b = random.randint(0, 255)
            g= random.randint(0, 255)
            r = random.randint(0, 255)

            newCreature = creature.img
            canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
            painting = ImageDraw.Draw(canvas)
            painting.polygon(points, (r,g,b,a), (r,g,b,a))
            newCreature.paste(canvas, canvas)

            newBoi = whatup.Boi(newCreature)
            returnPop.append(newBoi)
        return returnPop
