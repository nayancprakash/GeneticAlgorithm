import random
import cv2 as cv
import numpy
import species
from sys import argv

if __name__ == "__main__":
    sourceImage = cv.imread(argv[1])
    height, width, depth = sourceImage.shape
    amountShapes = 125
    amountSpecies = 20
    amountVertices = 3
    polyRadius = 50
    dnaLength = 4 + amountVertices*2 #BGRA + Vertices
    population = []
    drawing = []
    fitnessArray = []
    for i in range(0, amountSpecies):
        speciesDNA = []
        img = numpy.zeros((height, width, 3))
        for j in range(0, amountShapes):
            B = random.randint(0, 256) # B
            G = random.randint(0, 256) # G
            R = random.randint(0, 256) # R
            A = random.random() # alpha
            xAnchor = random.randint(0, width+1)
            yAnchor = random.randint(0, height+1)
            shapePoints = []
            DNA = [B, G, R, A]
            for k in range(0, amountVertices):

                point = [round(xAnchor+random.uniform(-1, 1)*polyRadius), round(yAnchor+random.uniform(-1, 1)*polyRadius)]
                shapePoints.append(point)
                DNA.extend(point)
                #shapePoints.append(round(yAnchor+random.uniform(-1, 1)*polyRadius))
            overlay = numpy.zeros((height, width, 3))
            cv.fillPoly(overlay, [numpy.array(shapePoints)], (B, G, R))
            img = img*(1-A)+overlay*A
            speciesDNA.extend(DNA)
        #drawing.append(img)
        #population.append(species)
        deltaB = sourceImage[:][:][0] - img[:][:][0]
        deltaG = sourceImage[:][:][1] - img[:][:][1]
        deltaR = sourceImage[:][:][2] - img[:][:][2]
        fitness = deltaB*deltaB + deltaG*deltaG + deltaR*deltaR
        fitness = numpy.sum(fitness)
        #fitnessArray.append(fitness)
        population.append(species.species(img, speciesDNA, fitness))
    #print(fitnessArray)
    population = sorted(population, key=lambda x: x.fitness, reverse=True)
    cv.imshow("Fittest Species", population[0].image)
    cv.waitKey(0)
    #print(population)
