crab_dict = dict()

with open("input.txt", "r") as crab_file:
    crabPositions = [int(crab_string) for crab_string in crab_file.read().strip().split(",")]
    for crab_position in crabPositions:
        try:
            crab_dict[crab_position] += 1
        except KeyError:
            crab_dict[crab_position] = 1
fuelCostGuesses = list()
fuelCost = 0
for guess in range(1, max(crabPositions) + 1):
    for position, crabCount in crab_dict.items():
        fuelCost += abs(guess-position) * crabCount # I bet there is a way smarter way to do this and I have no idea what it is :)
    fuelCostGuesses.append(fuelCost)
    fuelCost = 0
        
print(min(fuelCostGuesses))