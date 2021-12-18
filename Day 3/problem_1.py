columnSliders = [0]*12
with open("input.txt", "r") as bitstring_file:
    for bitstring in bitstring_file:
        bitstring = bitstring.strip()
        for index, char in enumerate(bitstring):
            columnSliders[index] += 1 if char == "1" else -1
gammaThing = int("".join([str(int(slider > 0)) for slider in columnSliders]), 2)
epsilonThing = (~gammaThing & 0xFFF)
print(gammaThing * epsilonThing)
