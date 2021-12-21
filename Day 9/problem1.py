class CaveFloorPoint:
    def __init__(self,height, leftNeighbour, upNeighbour):
        self.height = height
        self.risky = True
        self.risky = self.risky and (leftNeighbour is None or leftNeighbour.height > self.height)
        self.risky = self.risky and (upNeighbour is None or upNeighbour.height > self.height)
        if leftNeighbour is not None:
            leftNeighbour.risky = leftNeighbour.risky and (leftNeighbour.height < self.height)
        if upNeighbour is not None: 
            upNeighbour.risky = upNeighbour.risky and (upNeighbour.height < self.height)

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
            
print(sum([1 + point.height for point in floorPointsByCoords.values() if point.risky]))