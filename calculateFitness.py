import Species
import random
import numpy

def calculateFitness(population, img):
    fittest = None
    for species in population:
        # species.drawSpecies()
        fitness = 0
        delta = img - species.image
        # deltaB = img[:][:][0] - species.image[:][:][0]
        # deltaG = img[:][:][1] - species.image[:][:][1]
        # deltaR = img[:][:][2] - species.image[:][:][2]
        # fitness = deltaB*deltaB + deltaG*deltaG + deltaR*deltaR
        fitness = delta*delta
        fitness = numpy.sum(fitness)
        #for y in range(species.image.shape[0]):
            #for x in range(species.image.shape[1]):
                #deltaB = abs(img[y][x][0] - species.image[y][x][0])/16
                #deltaG = abs(img[y][x][1] - species.image[y][x][1])/16
                #deltaR = abs(img[y][x][2] - species.image[y][x][2])/16
                #fitness += deltaB*deltaB + deltaG*deltaG + deltaR*deltaR
        species.fitness = fitness
        #print(fitness)
    return
