import Species
import crossover
import mutation


def select (population, amount):

    populationFitness =[]*len(population)
    matingPool = []*amount

    i = 0
    for species in population:
        population[i] = species.getFitness()
        i+=1

    populationFitness.sort()

    i = 0
    for species in population:
        if species.fitness >= populationFitness[amount]:
            matingPool[i]=species
            i+=1
            # assume there wont be a tie



    return child




