horiz = 0
vert = 0
aim = 0

with open("input.txt", "r") as direction_file:
    direction_list = direction_file.read().splitlines(False)

for direction in direction_list:
    axis, quantity = direction.split()
    quantity = int(quantity)

    if (axis == "forward"):
        horiz += quantity
        vert += aim * quantity
    elif (axis == "up"):
        aim -= quantity
    else:
        aim += quantity

print(str(horiz*vert))
