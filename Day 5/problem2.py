def markHit(hitDict, point):
    try:
        hitDict[point] += 1
    except KeyError:
        hitDict[point] = 1
        
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
                markHit(hitMarkers, (beginCoords[0], y))
        elif beginCoords[1] == endCoords[1]:
            directionalModifier = 1 if endCoords[0] > beginCoords[0] else -1
            for x in range(beginCoords[0], endCoords[0] + directionalModifier, directionalModifier):
                markHit(hitMarkers, (x, beginCoords[1]))
        else:
            horizontalDirection = 1 if endCoords[0] > beginCoords[0] else -1
            verticalDirection = 1 if endCoords[1] > beginCoords[1] else -1
            currentPoint = beginCoords
            while(True):
                markHit(hitMarkers, currentPoint)                
                if currentPoint == endCoords:
                    break
                currentPoint = (currentPoint[0] + horizontalDirection, 
                                currentPoint[1] + verticalDirection)
                
            
print(len([hitCount for hitCount in hitMarkers.values() if hitCount > 1]))