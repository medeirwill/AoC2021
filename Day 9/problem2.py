class CaveFloorPoint:
    def __init__(self,height, leftNeighbour, upNeighbour):
        self.height = height
        self.risky = True
        self.toHigherGround = list()
        self.risky = self.risky and (leftNeighbour is None or leftNeighbour.height > self.height)
        self.risky = self.risky and (upNeighbour is None or upNeighbour.height > self.height)
        if leftNeighbour is not None:
            leftNeighbour.risky = leftNeighbour.risky and (leftNeighbour.height < self.height)
            if self.height != 9 and leftNeighbour.height != 9:
                if leftNeighbour.height > self.height:
                    self.toHigherGround.append(leftNeighbour)
                elif self.height > leftNeighbour.height:
                    leftNeighbour.toHigherGround.append(self)
        if upNeighbour is not None: 
            upNeighbour.risky = upNeighbour.risky and (upNeighbour.height < self.height)
            if self.height != 9 and upNeighbour.height != 9:
                if upNeighbour.height > self.height:
                    self.toHigherGround.append(upNeighbour)
                elif self.height > upNeighbour.height:
                    upNeighbour.toHigherGround.append(self)

def walkBasin(point, basinMembers):
    if point not in basinMembers:
        basinMembers.append(point)
        for uphillPoint in point.toHigherGround:
            walkBasin(uphillPoint, basinMembers)
    return len(basinMembers)
            
        
with open("input.txt", "r") as caveFloorFile:
    caveRows = [line.strip() for line in caveFloorFile.readlines()]

floorPointsByCoords = dict()
for rowNum, row in enumerate(caveRows):
    for columnNum, height in enumerate([int(heightString) for heightString in row]):
        try:
            leftNeighbour = floorPointsByCoords[(columnNum - 1, rowNum)]
        except KeyError:
            leftNeighbour = None
        try:
            upNeighbour = floorPointsByCoords[(columnNum, rowNum - 1)]
        except KeyError:
            upNeighbour = None
        
        floorPointsByCoords[(columnNum, rowNum)] = CaveFloorPoint(height, leftNeighbour, upNeighbour)

basinProducts = list()          
for riskyPoint in [point for point in floorPointsByCoords.values() if point.risky]:
    basinProducts.append(walkBasin(riskyPoint, list()))
    
basinProducts.sort(reverse=True)

finalProduct = 1
for i in range(3):
    finalProduct = finalProduct * basinProducts[i]
    
print(finalProduct)