import Species
import random

def calculateFitness(species, img):
    # speciesFit = []
    #for species in population:
    species.drawSpecies()
    fitness = 0
    for y in range(species.image.shape[0]):
        for x in range(species.image.shape[1]):
            deltaB = abs(img[y][x][0] - species.image[y][x][0])/16
            deltaG = abs(img[y][x][1] - species.image[y][x][1])/16
            deltaR = abs(img[y][x][2] - species.image[y][x][2])/16
            fitness += deltaB*deltaB + deltaG*deltaG + deltaR*deltaR
    species.fitness = fitness
    speciesFit = fitness
    #speciesFit.append(fitness)
    #speciesFit.sort()
    return speciesFit