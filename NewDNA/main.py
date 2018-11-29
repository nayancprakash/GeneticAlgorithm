import random
import cv2 as cv
import numpy
import species
from sys import argv
sourceImage = cv.imread(argv[1])
height, width, depth = sourceImage.shape
amountShapes = 150
amountSpecies = 20
amountVertices = 3
polyRadius = 150
cutoff = 15
mutationRate = 10/100
mutationChange =10
dnaLength = 4 + amountVertices*2 #BGRA + Vertices
strandLength = dnaLength*amountShapes
population = []
drawing = []
fitnessArray = []
maxerror = ((width*height*255)^2)*3
if __name__ == "__main__":



    def CreateSpecies():
        speciesDNA = []
        img = numpy.zeros((height, width, 3))
        fitness =0

        for j in range(0, amountShapes):
            ShapeDNA,img = CreateShapes(img)
            speciesDNA.extend(ShapeDNA)

        fitness = CalculateFit(img)

        Species = species.species(img, speciesDNA, fitness)
        return Species

    def CreateShapes(img):
        B = random.randint(0, 255)  # B
        G = random.randint(0, 255)  #
        R = random.randint(0, 255)  # R
        A = random.random() / 1000  # alpha
        xAnchor = random.randint(0, width + 1)
        yAnchor = random.randint(0, height + 1)
        shapePoints = []
        DNA = [B, G, R, A]

        for k in range(0, amountVertices):
            point = [round(xAnchor + random.uniform(-1, 1) * polyRadius),
                     round(yAnchor + random.uniform(-1, 1) * polyRadius)]
            shapePoints.append(point)
            DNA.extend(point)
        overlay = numpy.zeros((height, width, 3))
        cv.fillPoly(overlay, [numpy.array(shapePoints)], (B, G, R))
        img = img + overlay*A
        return DNA,img


    def DrawShape( img,DNA):
        shapePoints =[]
        # print(DNA)
        B = round(DNA[0])
        G = round(DNA[1])
        R = round(DNA[2])
        A = DNA[3]
        i = 4
        for k in range(0, amountVertices):
            point = [DNA[i],DNA[i+1]]
            shapePoints.append(point)
            i+=1

        overlay = numpy.zeros((height, width, 3))
        buff = numpy.array(shapePoints,)
        cv.fillPoly(overlay, numpy.int32([buff]), (B, G, R))
        img = img + overlay*A
        return img

    def CalculateFit(img):
        #print(sourceImage)
        #print(img)
        #print(img.shape)
        #print("hi")
        #print(sourceImage.shape)
        delta = sourceImage - (img*255)
        #print(delta.shape)
        #deltaB = delta[0][:][:][0]
        #deltaB = (sourceImage[0][:][:] - img[0][:][:])
        #print(deltaB)
        #print(deltaB.shape)
        #deltaG = sourceImage[:][:][1] - img[:][:][1]
        #print(deltaG)
        #deltaR = sourceImage[:][:][2] - img[:][:][2]
        #print(deltaR)
        #fitness = deltaB * deltaB + deltaG * deltaG + deltaR * deltaR
        fitness = delta*delta
        fitness = numpy.sum(fitness)
        #print(fitness)

        #fitness = 1 -(fitness/maxerror)

        return fitness

    def Mutate(dna):
        return dna

    for i in range(0, amountSpecies):
        population.append(CreateSpecies())

    # cv.imshow("Fittest Species", population[0].image)
    # cv.waitKey(0)
    counter =0
    while(counter <100):
        population = sorted(population, key=lambda x: x.fitness, reverse=False)
        print("Generation: %i Fitness: %f" % (counter, population[0].fitness))
        # cv.imshow("Fittest Species", population[0].image)
        # cv.waitKey(0)
        newPop = []
        newPop.append(population[0])
        for i in range(0,cutoff):
            for j in range(0,round(random.random()*5)):
                randomMate =random.randint(0,cutoff-1)
                newDna = []
                newimg = numpy.zeros((height, width, 3))
                p =0
                while(p < strandLength):
                    randInherit = random.random()
                    if randInherit >= 0.5:
                        newDna.extend(population[i].dna[p:p+dnaLength])
                        newimg =DrawShape(newimg,population[i].dna[p:p+dnaLength])
                    else:
                        newDna.extend(population[randomMate].dna[p:p + dnaLength])
                        newimg = DrawShape(newimg,population[i].dna[p:p+dnaLength])
                    p += dnaLength
                fit = CalculateFit(newimg)
                mutationSelect = random.random()
                if mutationSelect<= mutationRate:
                    newDna[0] +=(random.random()*mutationChange*2 -mutationChange)*255
                    if newDna[0] > 255:
                        newDna[0]= 255
                    elif newDna[0] < 0:
                        newDna[0] =0
                elif  mutationSelect <= 2*mutationRate:
                    newDna[1] += (random.random()*mutationChange*2 -mutationChange)*255
                    if newDna[1] > 255:
                        newDna[1] = 255
                    elif newDna[1] < 0:
                        newDna[1] = 0
                elif mutationSelect <= 3*mutationRate:
                    newDna[2] +=(random.random()*mutationChange*2 -mutationChange)*255
                    if newDna[2] > 255:
                        newDna[2] = 255
                    elif newDna[2] < 0:
                        newDna[2] = 0
                elif mutationSelect <= 4*mutationRate:
                    newDna[3] +=(random.random()*mutationChange*2 -mutationChange)*(1/100)
                    if newDna[3] > 1:
                        newDna[3] = 1
                    elif newDna[3] < 0:
                        newDna[3] = 0
                elif mutationSelect<= 5*mutationRate:
                    newDna[4] +=(random.random()*mutationChange*2 -mutationChange)*height
                elif mutationSelect <= 6*mutationRate:
                    newDna[5] +=(random.random()*mutationChange*2 -mutationChange)*height
                elif mutationSelect <= 7*mutationRate:
                    newDna[6] +=(random.random()*mutationChange*2 -mutationChange)*width
                elif mutationSelect <= 8*mutationRate:
                    newDna[7] +=(random.random()*mutationChange*2 -mutationChange)*height
                elif mutationSelect<= 9*mutationRate:
                    newDna[8] +=(random.random()*mutationChange*2 -mutationChange)*width
                elif mutationSelect <= 10*mutationRate:
                    newDna[9] +=(random.random()*mutationChange*2 -mutationChange)*height
                newSpecies = species.species(newimg, newDna, fit)
                newPop.append(newSpecies)

        counter +=1
        population =[]
        population =newPop

        cv.imshow("Fittest Species", newPop[0].image)
        cv.waitKey(1)


