from shapely.ops import unary_union, LineString, MultiLineString
segmentList = list()
with open("input.txt", "r") as line_file:
    for line in line_file:
        line = line.strip()
        beginString, endString = line.split(" -> ")
        beginCoords = tuple(int(x) for x in beginString.split(","))
        endCoords = tuple(int(x) for x in endString.split(","))
        if beginCoords[0] == endCoords[0] or beginCoords[1] == endCoords[1]:
            segmentList.append(LineString([beginCoords, endCoords]))

overlapObject = segmentList[0].intersection(segmentList[1])
unionObject = unary_union(segmentList[0:1])
overlapCoordsSet = set(overlapObject.coords)

for i in range(2, len(segmentList)):
    overlapObject = unionObject.intersection(segmentList[i])
    try:
        overlapCoordsSet.add(overlapObject.coords)
    except NotImplementedError:
        for geom in overlapObject.geoms:
            overlapCoordsSet.add(geom.coords)
            
    unionObject = unary_union([unionObject, segmentList[i]])

print(len(overlapCoordsSet))        