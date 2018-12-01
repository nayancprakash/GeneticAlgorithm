import random
import Species

def crossover(population, amountFit):
    bredSpecies = []
    for i in range(0, amountFit):
        for j in range(0, amountFit):
            if population[i] != population[j]:
                bredSpecies.append(breed(population[i], population[j]))
    return bredSpecies


def breed(parent1, parent2):
    genes = []
    for i in range(0, len(parent1.shapes)):
        if random.random() < 0.5:
            genes.append(parent1.shapes[i])
            #genes.append(random.choice(parent1.shapes))
        else:
            genes.append(parent2.shapes[i])
            #genes.append(random.choice(parent2.shapes))
    return Species.Species(genes, parent1.height, parent1.width)
