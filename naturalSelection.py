import Species

def naturalSelection(pop,popFit, amount):
    mating = []

    for species in pop:
        if species.fitness <= popFit[amount-1]:
            mating.append(species)
            if species.fitness == popFit[0]:
                fittest = species

    return (mating,fittest)





