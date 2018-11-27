import Shapes
import Species

# create n species
def runGenesis(n, amountShapes, height, width, randAlpha):
    speciesList = []
    for i in range(n):
        shapeList = []
        for j in range(amountShapes):
            shapeList.append(Shapes.Shapes(height, width, randAlpha))
        speciesList.append(Species.Species(shapeList, height, width))
    return speciesList
