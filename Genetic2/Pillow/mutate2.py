from PIL import Image, ImageDraw
import random
import Species

def mutate(population, mutationRate, mutationAmount):
    width, height = population[0].image.size
    #for species in population:
    populationList = []
    for i in range(0, len(population)):
        #for shape in species.shapes:
        for j in range(0, len(population[i].shapes)):
            #for point in shape.points:
            for k in range(0, len(population[i].shapes[j].points)):
                if random.random() < mutationRate:
                    negOrPos = random.choice([-1, 1])
                    x, y = population[i].shapes[j].points[k]
                    x += negOrPos*x*mutationAmount
                    y += negOrPos*y*mutationAmount
                    population[i].shapes[j].points[k] = (round(x), round(y))
            r, g, b, a = population[i].shapes[j].color
            if random.random() < mutationRate:
                negOrPos = random.choice([-1, 1])
                r += negOrPos*r*mutationAmount
            if random.random() < mutationRate:
                negOrPos = random.choice([-1, 1])
                g += negOrPos*g*mutationAmount
            if random.random() < mutationRate:
                negOrPos = random.choice([-1, 1])
                b += negOrPos*b*mutationAmount
            if random.random() < mutationRate:
                negOrPos = random.choice([-1, 1])
                a += negOrPos*a*mutationAmount
            population[i].shapes[j].color = (round(r), round(g), round(b), round(a))
            # population[i].shapes[j].color = (0, 0, 0, 255)

        population[i].drawSpecies()
            # print(population[i].shapes[j].g)

            # print("I want a spatula in my anus")
        populationList.append(population[i])
    return populationList
