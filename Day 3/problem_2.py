def ratingFinder(bitstringArray, depth, keepAbundant):
    zeroList = list()
    oneList = list()
    for bitstring in bitstringArray:
        if bitstring[depth] == "1":
            oneList.append(bitstring)
        else:
            zeroList.append(bitstring)

    if (keepAbundant):
        keeperList = zeroList if len(zeroList) > len(oneList) else oneList
    else:
        keeperList = oneList if len(oneList) < len(zeroList) else zeroList

    return keeperList[0] if len(keeperList) == 1 else ratingFinder(keeperList, depth + 1, keepAbundant)


with open("input.txt", "r") as bitstringFile:
    bitstringArray = bitstringFile.read().splitlines()

oxygenRating = ratingFinder(bitstringArray, 0, True)
carbonRating = ratingFinder(bitstringArray, 0, False)

print(int(oxygenRating, 2) * int(carbonRating, 2))
