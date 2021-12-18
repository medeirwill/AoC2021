uniqueSections = {2, 4, 3, 7}
targetNumeralCount = 0
with open("input.txt", "r") as clockFile: 
    for analyzedSection in (line.split("|")[1].strip() for line in clockFile):
        for numeralString in analyzedSection.split():
            if len(numeralString) in uniqueSections: 
                targetNumeralCount += 1

print(targetNumeralCount)