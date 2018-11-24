import Species

def naturalSelection(pop, popFit, amount):
    mating = [0]*(amount)
    i=0
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





