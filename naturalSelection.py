import Species
import crossover

def naturalSelection(pop, popFit, amount):
    mating = [0]*(amount)
    i = 0
    for species in pop:
        if species.fitness <= popFit[amount-1]:
            if i < amount:
                mating[i] = species
                i += 1
            if species.fitness == popFit[0]:
                fittest = species
        else:
            species.image = None
            species.shapes= None
            species = None


    return (mating,fittest)

# def naturalSelection(pop, popFit, amount):
#     population = []
#     for species1 in pop:
#         for species2 in pop:
#             if species1 != species2:
#                 population.append(cross(species1, species2))
#     return population
