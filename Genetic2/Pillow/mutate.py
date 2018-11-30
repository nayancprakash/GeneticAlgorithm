import random


def mutate(population, mutationRate, mutationAmount):
    width, height = population[0].image.size
    mutatedSpecies = []
    for i in range(0, len(population)):
        # genes = species.shapes
        # for gene in genes:
        #     for point in gene.points:
        #         if random.random() < mutationRate:
        #             point = [round(point[0]*mutationAmount), round(point[0]*mutationAmount)]
        #     for color in gene.color:
        #         if random.random() < mutationRate:
        #             color
        for j in range (0, len(population[i].shapes)):
            for k in range(0, len(population[i].shapes[j].points)):
                if random.random() < mutationRate:
                    negOrPos1 = random.choice([-1, 1])
                    negOrPos2 = random.choice([-1, 1])
                    #population[i].shapes[j].points[k] += [negOrPos1*round(population[i].shapes[j].points[k][0]*mutationAmount), negOrPos2*round(population[i].shapes[j].points[k][1]*mutationAmount)]
                    population[i].shapes[j].points[k][0] += negOrPos1*round(population[i].shapes[j].points[k][0]*mutationAmount)
                    population[i].shapes[j].points[k][1] += negOrPos2*round(population[i].shapes[j].points[k][1]*mutationAmount)
                    break
            if random.random() < mutationRate:
                negOrPos = random.choice([-1, 1])
                population[i].shapes[j].alpha += negOrPos*population[i].shapes[j].alpha * mutationAmount
                if population[i].shapes[j].alpha < 0:
                    population[i].shapes[j].alpha = 0.1;
                if population[i].shapes[j].alpha > 1:
                    population[i].shapes[j].alpha = 1;
                    break
            for k in range(0, len(population[i].shapes[j].color)):
                if random.random() < mutationRate:
                    negOrPos = random.choice([-1, 1])
                    #population[i].shapes[j].color = [0, 0, 255]
                    #print("mutate color")
                    population[i].shapes[j].color[k] += negOrPos*round(population[i].shapes[j].color[k] * mutationAmount)
                    if population[i].shapes[j].color[k] < 0:
                        population[i].shapes[j].color[k] = 0
                    if population[i].shapes[j].color[k] > 255:
                        population[i].shapes[j].color[k] = 255
                    break
        mutatedSpecies.append(population[i])
    return mutatedSpecies
