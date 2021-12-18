horiz = 0
vert = 0

with open("input.txt", "r") as direction_file:
    direction_list = direction_file.read().splitlines(False)

for direction in direction_list:
    axis, quantity = direction.split()
    quantity = int(quantity)

    if (axis == "forward"):
        horiz += quantity
    elif (axis == "up"):
        vert -= quantity
    else:
        vert += quantity

print(str(horiz*vert))
