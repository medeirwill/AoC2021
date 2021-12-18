fishPopulationsToday = [0] * 9 
with open("input.txt", "r") as lanternfish_file:
    for age in [int(ageString) for ageString in lanternfish_file.read().strip().split(",")]:
        fishPopulationsToday[age] += 1

fishPopulationsTomorrow = [0] * 9 
for day in range(256):
    for index, pop in enumerate(fishPopulationsToday):
        if index == 0:
            fishPopulationsTomorrow[6] += pop
            fishPopulationsTomorrow[index] = 0
        fishPopulationsTomorrow[index-1] += fishPopulationsToday[index]
    fishPopulationsToday = fishPopulationsTomorrow.copy()
    fishPopulationsTomorrow = [0] * 9

print(sum(fishPopulationsToday))

# for problem 1 just change the range upper bound to 80
