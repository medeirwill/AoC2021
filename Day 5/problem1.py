hitMarkers = dict()
with open("input.txt", "r") as line_file:
    for line in line_file:
        line = line.strip()
        beginString, endString = line.split(" -> ")
        beginCoords = tuple(int(x) for x in beginString.split(","))
        endCoords = tuple(int(x) for x in endString.split(","))
        if beginCoords[0] == endCoords[0]:
            directionalModifier = 1 if endCoords[1] > beginCoords[1] else -1
            for y in range(beginCoords[1], endCoords[1] + directionalModifier, directionalModifier):
                try:
                    hitMarkers[(beginCoords[0], y)] += 1
                except KeyError:
                    hitMarkers[(beginCoords[0], y)] = 1
        elif beginCoords[1] == endCoords[1]:
            directionalModifier = 1 if endCoords[0] > beginCoords[0] else -1
            for x in range(beginCoords[0], endCoords[0] + directionalModifier, directionalModifier):
                try:
                    hitMarkers[(x, beginCoords[1])] += 1
                except KeyError:
                    hitMarkers[(x, beginCoords[1])] = 1
            
print(len([coords for (coords, hits) in hitMarkers.items() if hits > 1]))